#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * run_infinite_loop - Run and infinite while loop
 *
 * Return: 0
 */

int run_infinite_loop(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - create 5 zombie processes
 *
 * Return: 0
 */
int main(void)
{
	pid_t pid;
	char counter = 0;

	while (counter < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			counter++;
		}
		else
			exit(0);
	}
	run_infinite_loop();
	return (EXIT_SUCCESS);
}
