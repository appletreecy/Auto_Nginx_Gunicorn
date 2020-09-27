from flask import Blueprint
from flask import render_template, request, flash
from flaskblog.models import Post
from flask_login import login_required
from flaskblog.posts.forms import PostForm
from flaskblog.bpsRest import *
import paramiko
from subprocess import check_output
import re

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/about2")
def about2():
    return render_template('about2.html', title='About2')
	

@main.route("/attack/1", methods=['GET', 'POST'])
@login_required
def attack():
    form = PostForm()
#    flash('Your attack has been started!', 'success')
    bps = BPS('172.16.14.28', 'admin', 'admin')
    bps.login()
    # login
    # showing current port reservation state
    bps.portsState()
    # reserving the ports.
    bps.reservePorts(slot = 1, portList = [0,1,2,3], group = 1, force = True)
    # running the canned test 'AppSim' using group 1
    # please note the runid generated. It will be used for many more functionalities
    runid = bps.runTest(modelname = 'Victor-ESA-Test-Spam', group = 1)
    # showing progress and current statistics
    progress = 0
    while (progress < 100):
    	progress = bps.getRTS(runid)
    	time.sleep(1)
    # showing the test result (Pass/Fail)
    # a sleep is put here because we do not immediately get the test results.
    # inserting a sleep to allow for the data to be stored in the database before retrieval
    time.sleep(1)
    bps.getTestResult(runid)
	
    runid = bps.runTest(modelname = 'Cyber-Landing-Traffic', group = 1)
    # showing progress and current statistics
    progress = 0
    while (progress < 100):
    	progress = bps.getRTS(runid)
    	    if progress is None:
    	        progress = 1
    	time.sleep(1)
    time.sleep(1)
    bps.getTestResult(runid)
	
    # logging out
    bps.logout()
    flash('Your attack 1 has been launched!', 'success')

    return render_template('about.html', title='test', form=form)
	
@main.route("/attack/2", methods=['GET', 'POST'])
@login_required
def attack2():
    form = PostForm()
    ip = '172.105.123.219'
    username ='root'
    password = 'C1sc0123@CL'
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(ip,username=username, password=password, look_for_keys=True, allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()
    output = remote_conn.recv(1000)
    print (output)
    
#    remote_conn.send("/usr/bin/python3 /root/temp/test1.py")
    remote_conn.send("uname -a\r")
    output1 = remote_conn.recv(2000)
    time.sleep(1)
    print (output1)
    flash(output1, 'success')
	
    return render_template('about.html', title='test', form=form)
	
@main.route("/attack/3", methods=['GET', 'POST'])
@login_required
def attack3():
    form = PostForm()
    ret = check_output(["python3","/home/scao/autocli/test2.py"])
    print(ret)
    flash(ret, 'success')
	
    return render_template('about.html', title='test', form=form)


@main.route("/attack/4", methods=['GET', 'POST'])
@login_required
def attack4():
    form = PostForm()
#    flash('Your attack has been started!', 'success')
    bps = BPS('172.16.14.28', 'admin', 'admin')
    bps.login()
    # login
    # showing current port reservation state
    bps.portsState()
    # reserving the ports.
    bps.reservePorts(slot = 1, portList = [0,1,2,3], group = 1, force = True)
    # running the canned test 'AppSim' using group 1
    # please note the runid generated. It will be used for many more functionalities
    runid = bps.runTest(modelname = 'Victor-ESA-Test-Spam', group = 1)
    # showing progress and current statistics
    progress = 0
    while (progress < 100):
        progress = bps.getRTS(runid)
        time.sleep(1)
    # showing the test result (Pass/Fail)
    # a sleep is put here because we do not immediately get the test results.
    # inserting a sleep to allow for the data to be stored in the database before retrieval
    time.sleep(1)
    bps.getTestResult(runid)
    
    # logging out
    bps.logout()
    flash('Your attack 4 has been launched!', 'success')

    return render_template('about.html', title='test', form=form)

@main.route("/attack/5", methods=['GET', 'POST'])
@login_required
def attack5():
    form = PostForm()
    ret = check_output(["python3","/home/scao/autocli/single_bpsProfile.py"])
    
    flash('Attatck 5 has been launched', 'success')


@main.route("/attack/status", methods=['GET', 'POST'])
@login_required
def attack_status():
    form = PostForm()
    bps = BPS('172.16.14.28', 'admin', 'admin')
    bps.login()
    ret = bps.runningTestInfo()
    if len(ret) == 2:
        flash('The BPS attack status is not running/starting', 'success')
        #flash(len(ret))

    else:
        progress = re.search('Progress: \[(\d+)\]', ret).groups()[0]
        
        #print(progress)
        flash('The BPS attack status is: ' + progress + '%', 'success')
        #flash(ret)
    bps.logout()
    
    return render_template('attack_status.html', title='test', form=form)

@main.route("/attack/stop", methods=['GET', 'POST'])
@login_required
def attack_stop():
    form = PostForm()
    bps = BPS('172.16.14.28', 'admin', 'admin')
    bps.login()
    ret = bps.runningTestInfo()
    testid = re.search('TestId:\s\[(\w+-\d+)\]', ret).groups()[0]
    bps.stopTest(testid=testid)

    time.sleep(1)

    
    # logging out
    bps.logout()
    flash('The current BPS attack has been stopped!', 'success')

    return render_template('attack_status.html', title='test', form=form)

