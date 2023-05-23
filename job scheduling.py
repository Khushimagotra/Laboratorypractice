import sys

def job_scheduling(jobs):
  """
  Job scheduling algorithm to find the optimal schedule for a set of jobs.

  Args:
    jobs: A list of jobs. Each job is a tuple of (start time, end time, profit).

  Returns:
    A list of jobs in the optimal schedule.
  """

  # Sort the jobs by start time.
  jobs.sort(key=lambda j: j[0])

  # Create a list to store the jobs that have been scheduled.
  scheduled_jobs = []

  # While there are jobs that have not been scheduled:
  while jobs:
    # Find the job with the earliest start time that has not been scheduled.
    current_job = min(jobs, key=lambda j: j[0])

    # Add the current job to the scheduled jobs.
    scheduled_jobs.append(current_job)

    # Remove the current job from the list of jobs.
    jobs.remove(current_job)

  # Return the list of scheduled jobs.
  return scheduled_jobs


def main():
  """
  Main function.

  This function prompts the user to enter the number of jobs and the start and end times for each job. It then uses the job scheduling algorithm to find the optimal schedule for the jobs and prints the schedule.
  """

  num_jobs = int(input("Enter the number of jobs: "))

  jobs = []

  for _ in range(num_jobs):
    start, end, profit = map(int, input().split())
    jobs.append((start, end, profit))

  scheduled_jobs = job_scheduling(jobs)

  print("The optimal schedule is:")
  for job in scheduled_jobs:
    print(job)


if __name__ == "__main__":
  main()