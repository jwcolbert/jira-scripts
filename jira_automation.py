#!/usr/bin/env python

import json
import request
import datetime
from jira import JIRA
import re
import sys
import os


menu_actions = {}
user = os.getenv("JIRA_USER")
password = os.getenv("JIRA_PASSWORD")
jiraenv = os.getenv("JIRA_ENV")

jira = JIRA(jiraenv, basic_auth=(user, password))

def main_menu():
    os.system('clear')
    
    print("Welcome,\n")
    print("Please choose your option:")
    print("1. Create Sprints")
    print("\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
 
    return

def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()

def createSprints():
    print("Automated Sprint Creation")
    board_id = input("Jira Board ID: ")
    print("Sprint Name Format: (Example: PI1)")
    sprint_name = input("Sprint Name Pattern: ")
    start_date = input("Start Date (MM/DD/YY): ")
#    sprint_length = input("Sprint Length in days (Ex: 13): " )
    sprint_length = 13
    sprint_iterations = input("Number of sprints to generate: ")
    i = 0
    while i < int(sprint_iterations):
        if i == 0:
            sprintStart = datetime.datetime.strptime(start_date, "%m/%d/%y")
#            sprintEnd = sprintStart + datetime.timedelta(days=int(sprint_length))
        else:
            sprintStart = sprintEnd + datetime.timedelta(days=1)
        sprintEnd = sprintStart + datetime.timedelta(days=int(sprint_length))
        sprintName = sprint_name + " Sprint " + str(i+1) + " " + sprintStart.strftime("%b%d")
        jira.create_sprint(sprintName, board_id, sprintStart.strftime("%d/%b/%Y 9:00 AM"), sprintEnd.strftime("%d/%b/%Y 5:00 PM"))
        i += 1

menu_actions = {
    'main_menu': main_menu,
    '1': createSprints
}

if __name__ == "__main__":
    main_menu()
