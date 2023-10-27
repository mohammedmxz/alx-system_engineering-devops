#include <stdio.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - entry point to a program that creates
 * zombie processes
 * Return: always 0
 */
int main(void)
{
	unsigned int n = 0;
	pid_t pid = getppid();

	do {
		pid = fork();
		if (pid == 0)
			printf("Zombie process created, PID: %u\n", getpid());

		n++;
	} while (n < 5 && pid != 0);

	if (pid != 0)
		infinite_while();

	return (0);
}

/**
 * infinite_while - an infinite loop
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
