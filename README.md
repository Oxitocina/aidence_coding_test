# aidence_coding_test

Console Tasker 
========================

<h1>Instructions to run my proposed solution to this exercise:</h1>
<p>This is a command line version of the exercise proposed. All interactions will be through text commands and all results will be printed in the console.</p>
<ul>
    <li> Make sure python 3.8 is installed in the pc (should work with 3.7 too, but it was developed and tested in 3.8).</li>
    <li> Clone repository.</li>
    <li> Go to the main directory of the project (aidence_coding_test).</li>
    <li> Open a terminal.</li>
    <li> Run "pip install -r requirements.txt" to install dependencies.</li>
    <li> Run "pytest test/" to run the tests.</li>
    <li> Run "python __main__.py" to run the actual program.</li>
    <li> The existing user in the database is Juan.</li>
</ul>

<h1>Commands to operate the script:</h1>
<ul>
    <li><b>{user name}</b> This command returns a lists of tasks for given user. (including title, description, status and unique identifier aka uid)</li>
    <li><b>{user name} -> {title}:{description} </b> This command creates a task with given title and description</li>
    <li><b>{user name} edit {task uid}:{title}:{description} </b> This command edits given task (uid) with given title and description</li>
    <li><b>{user name} complete {task uid}</b> This command completes given task (uid) changing its status</li>
</ul>