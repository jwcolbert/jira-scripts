# Jira Sprint Creation

## Installation Requirements
This script requires Python3

## Usage
**The following Environment Variables are required to be set prior to executing the script**
- JIRA_USER: *Your Atlassian account username (ex: john.smith@atlassian.net)*
- JIRA_TOKEN: *An Atlassian API Token*
- JIRA_ENV: *Your Jira Cloud instance URL (ex: https://example.atlassian.net)*

```
pip install -r requirements.txt
export JIRA_ENV="https://example.atlassian.net"
export JIRA_USER="john.smith@example.com"
export JIRA_TOKEN="xxxxxxxx"
python jira_automation.py
```

### Parameters:
- **Jira Board ID:** The Jira Board you want the sprints associated with. Example, a board located at "https://example.atlassian.net/secure/RapidBoard.jspa?rapidView=206" is board *206*
- **Sprint Name Pattern:** This will determine how your sprints are named. The pattern is whatever you enter here + Spring # + the sprint start date. An example would be if I enter "TeamX" as my Sprint Name Pattern and it starts on September 26th, my sprint name in Jira will be ***TeamX Sprint 1 Sep26***. The sprint numbers and start dates will increment accordingly depending on how many sprints you generate.
- **Sprint Start Date:** Entered in MM/DD/YY Format. Sprints are setup to start at 9am on the start date and will end 13 days later at 5:00pm. So for example, if you start a sprint on Wednesday the 1st, it will start at 9am and end Tuesday the 14th at 5pm.
- **Number of Sprints:** The number of sprints you want to generate