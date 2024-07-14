#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

typedef struct {
    int priority;
    double transmission_time;
    int period;
} Message;

int read_input_file(const char *filename, int *n, double *tau, Message **messages) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        perror("Error opening file");
        return 1;
    }

    fscanf(file, "%d", n);
    fscanf(file, "%lf", tau);

    *messages = (Message *)malloc(*n * sizeof(Message));
    if (!*messages) {
        perror("Memory allocation failed");
        fclose(file);
        return 1;
    }

    for (int i = 0; i < *n; ++i) {
        fscanf(file, "%d %lf %d", &((*messages)[i].priority), &((*messages)[i].transmission_time), &((*messages)[i].period));
    }

    fclose(file);
    return 0;
}

void findworstcase(int n, double tau, Message *messages) {
    printf("Number of messages: %d\n", n);
    printf("Tau: %f\n", tau);
    double min_sum = 1000;
    int *min_message = (int *)malloc(n * sizeof(int));
    int num_iterations = 2000000;
    srand(time(NULL));

    for (int iter = 0; iter < num_iterations; ++iter) {
        // Shuffle priorities
        for (int i = 0; i < n; ++i) {
            int j = rand() % n;
            int temp = messages[i].priority;
            messages[i].priority = messages[j].priority;
            messages[j].priority = temp;
        }

        double final_sum = 0;
        for (int i = 0; i < n; ++i) {
            double max = 0;
            for (int j = 0; j < n; ++j) {
                if (messages[j].priority >= messages[i].priority) {
                    if (messages[j].transmission_time > max) {
                        max = messages[j].transmission_time;
                    }
                }
            }

            double sum = 0;
            double q = max;
            for (int j = 0; j < n; ++j) {
                if (messages[j].priority < messages[i].priority) {
                    sum += ceil((q + tau) / messages[j].period) * messages[j].transmission_time;
                }
            }

            while (q != max + sum && (max + sum + messages[i].transmission_time) <= messages[i].period) {
                q = max + sum;
                sum = 0;
                for (int j = 0; j < n; ++j) {
                    if (messages[j].priority < messages[i].priority) {
                        sum += ceil((q + tau) / messages[j].period) * messages[j].transmission_time;
                    }
                }
            }

            if ((max + sum + messages[i].transmission_time) > messages[i].period) {
                final_sum = -1;
                break;
            } else {
                final_sum += q + messages[i].transmission_time;
            }
        }

        if (final_sum != -1 && final_sum < min_sum) {
            min_sum = final_sum;
            for (int i = 0; i < n; ++i) {
                min_message[i] = messages[i].priority;
            }
        }
    }

    printf("Minimum sum: %f\n", min_sum);
    printf("Priority with minimum sum: ");
    for (int i = 0; i < n; ++i) {
        printf("%d ", min_message[i]);
    }
    printf("\n");

    free(min_message);
}

int main() {
    const char *input_filename = "input.dat";
    int n;
    double tau;
    Message *messages;

    if (read_input_file(input_filename, &n, &tau, &messages) == 0) {
        findworstcase(n, tau, messages);
        free(messages);
    }

    return 0;
}