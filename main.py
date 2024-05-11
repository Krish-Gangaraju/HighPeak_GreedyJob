class Job:
    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self.profit = profit

# Input is a target job
# I am returning the index of the most recent job that ends before the start time of the target job
def binary_search(jobs, targetJob):
    left = 0 
    right = len(jobs) - 1
    target = targetJob.start
    while left <= right:
        mid = (left + right) // 2
        if jobs[mid].end <= target:
            left = mid + 1
        else:
            right = mid - 1
    return right


def max_earnings(jobs):
    # Sorts by the end time (watched youtube video to find out this is most efficient)
    jobs = sorted(jobs, key=lambda job: job.end)

    num_jobs = len(jobs)
    maxTable = [0] * num_jobs
    maxTable[0] = jobs[0].profit

    for i in range(1, num_jobs):
        previousJob = binary_search(jobs, jobs[i])
        # print(previousJob)

        newEarnings = jobs[i].profit    # This iteration of earnings (apart from the first job)
        if previousJob != -1:    # If there is a job that does not have time conflicts then
            newEarnings += maxTable[previousJob]  # Increment that previous job to this iteration of profits
        maxTable[i] = max(newEarnings, maxTable[i - 1])    # If this iteration of earnings is more then add this OR keep the previous max

    # List of the max earnings after considering every new job. The last element is the max Lokesh can earn
    # print(maxTable)


    # This section is to see which jobs Lokesh will take to maximise earnings
    selectedJobs = []
    i = num_jobs - 1
    while i >= 0:
        if i == 0 or maxTable[i] != maxTable[i - 1]:    # If maxTable of i and i - 1 are same that means the new job did not help in maximising profits so when they are different
            selectedJobs.append(jobs[i])    # We append this job to the list of jobs Lokesh will select
            previousJob = binary_search(jobs, jobs[i])    # It doesn't make sense to decrement by 1 here, instead we go back to the previous job that has no time conflicts
            i = previousJob
        else:
            i -= 1
    return maxTable[-1], selectedJobs  # Return max earnings and the jobs Lokesh will take to maximise earnings


def main():
    inputString1 = "0900,1030,100,1000,1200,500,1100,1200,300"  # Sample Input 1
    inputString2 = "0900,1000,250,0945,1200,550,1130,1500,150"  # Sample Input 2
    inputString3 = "0900,1030,100,1000,1200,100,1100,1200,100"  # Sample Input 3

    jobInformation = inputString1.split(',')
    num_jobs = len(jobInformation) // 3
    jobs = []

    # Makes the input string into (length // 3) Job objects
    for i in range(num_jobs):
        start = int(jobInformation[i * 3])
        end = int(jobInformation[i * 3 + 1])
        earnings = int(jobInformation[i * 3 + 2])
        jobs.append(Job(start, end, earnings))

    lokeshEarnings, lokeshJobs = max_earnings(jobs)
    jobsLeft = set(jobs) - set(lokeshJobs)
    earningsLeft = sum(job.profit for job in jobsLeft)

    print("The number of tasks and earnings available for others:")
    print(f"Task: {len(jobsLeft)}")
    print(f"Earnings: {earningsLeft}")
    print(f"Lokesh Makes: {lokeshEarnings}")

main()
