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

bpspassword = 'cyberland123'


def launchBpsAttack(attackName):
    bps = BPS('172.16.14.28', 'admin', bpspassword)
    bps.login()
    # login
    # showing current port reservation state
    bps.portsState()
    # reserving the ports.
    bps.reservePorts(slot=1, portList=[0, 1, 2, 3], group=1, force=True)
    # running the canned test 'AppSim' using group 1
    # please note the runid generated. It will be used for many more functionalities
    runid = bps.runTest(modelname=attackName, group=1)
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


@main.route("/attack/apt1", methods=['GET', 'POST'])
@login_required
def apt1():
    form = PostForm()
    launchBpsAttack("Victor-Zeus-CNC-Sourcefire")
    time.sleep(1)
    launchBpsAttack("Victor-SSH-DLP-Attack")

    flash('Your APT 1 has been launched!', 'success')

    return render_template('apt.html', title='test', form=form)


@main.route("/attack/apt2", methods=['GET', 'POST'])
@login_required
def apt2():
    form = PostForm()
    launchBpsAttack("Victor-ESA-Bad-Keyword")
    time.sleep(1)
    launchBpsAttack("Victor-WSA-Malware-Web-Site")
    time.sleep(1)
    launchBpsAttack("Victor-Malware-ZPACK")

    flash('Your APT 2 has been launched!', 'success')

    return render_template('apt.html', title='test', form=form)


@main.route("/attack/apt3", methods=['GET', 'POST'])
@login_required
def apt3():
    form = PostForm()
    launchBpsAttack("Victor-Web-Attack")
    time.sleep(1)
    launchBpsAttack("Victor-ESA-Credit-Card")
    time.sleep(1)
    launchBpsAttack("Victor-IRC-DLP")

    flash('Your APT 3 has been launched!', 'success')

    return render_template('apt.html', title='test', form=form)


@main.route("/attack/apt4", methods=['GET', 'POST'])
@login_required
def apt4():
    form = PostForm()
    launchBpsAttack("Victor-Adobe-Malware-Server-Client")
    time.sleep(1)
    launchBpsAttack("Victor-SMB-DLP-Attack")

    flash('Your APT 4 has been launched!', 'success')

    return render_template('apt.html', title='test', form=form)


@main.route("/attack/apt5", methods=['GET', 'POST'])
@login_required
def apt5():
    form = PostForm()
    launchBpsAttack("Victor-Synful-Knock-Attack")
    time.sleep(1)
    launchBpsAttack("Victor-DataLeak-FTP")

    flash('Your APT 5 has been launched!', 'success')

    return render_template('apt.html', title='test', form=form)


@main.route("/attack/apt6", methods=['GET', 'POST'])
@login_required
def apt6():
    form = PostForm()
    launchBpsAttack("Victor-Bot-to-Botmaster-Zeus")
    time.sleep(1)
    launchBpsAttack("Victor-Botmaster-to-bot-IOS-Trojan")

    flash('Your APT 6 has been launched!', 'success')

    return render_template('apt.html', title='test', form=form)


@main.route("/attack/apt7", methods=['GET', 'POST'])
@login_required
def apt7():
    form = PostForm()
    launchBpsAttack("Victor-Ransom-Attack")
    time.sleep(1)
    launchBpsAttack("Victor-Duqu-Botnet-DLP")

    flash('Your APT 7 has been launched!', 'success')

    return render_template('apt.html', title='test', form=form)


@main.route("/attack/apt8", methods=['GET', 'POST'])
@login_required
def apt8():
    form = PostForm()
    launchBpsAttack("Victor-bash-attack")
    time.sleep(1)
    launchBpsAttack("Victor-DDOS ICMP Flood Attack")

    flash('Your APT 8 has been launched!', 'success')

    return render_template('apt.html', title='test', form=form)


@main.route("/attack/apt9", methods=['GET', 'POST'])
@login_required
def apt9():
    form = PostForm()
    launchBpsAttack("Victor-Carbanak-Attack")
    time.sleep(1)
    launchBpsAttack("Victor-DataLeak-HTTPS")

    flash('Your APT 9 has been launched!', 'success')

    return render_template('apt.html', title='test', form=form)

# This the part for the Demo Routes


@main.route("/attack/netflow_demo", methods=['GET', 'POST'])
@login_required
def netflow_demo():
    form = PostForm()
    ip = '172.16.14.38'
    port = 22
    username = 'root'
    password = 'toor'
    cmd = '/root/netflow_script.sh'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password)

    stdin, stdout, stderr = ssh.exec_command(cmd)
    outlines = stdout.readlines()
    resp = ''.join(outlines)
    print(resp)
    flash(resp, 'success')

    return render_template('about_demo.html', title='test', form=form)


@main.route("/attack/threatIntel_demo", methods=['GET', 'POST'])
@login_required
def threatIntel_demo():
    form = PostForm()
    ip = '172.16.14.39'
    port = 22
    username = 'root'
    password = 'toor'
    cmd = '/root/threat_intel.sh'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password)

    stdin, stdout, stderr = ssh.exec_command(cmd)
    outlines = stdout.readlines()
    resp = ''.join(outlines)
    print(resp)
    flash(resp, 'success')

    return render_template('about_demo.html', title='test', form=form)


@main.route("/attack/cl_bps_demo", methods=['GET', 'POST'])
@login_required
def cl_bps_demo():
    form = PostForm()
#    flash('Your attack has been started!', 'success')
    bps = BPS('172.16.14.28', 'admin', bpspassword)
    bps.login()
    # login
    # showing current port reservation state
    bps.portsState()
    # reserving the ports.
    bps.reservePorts(slot=1, portList=[0, 1, 2, 3], group=1, force=True)
    # running the canned test 'AppSim' using group 1
    # please note the runid generated. It will be used for many more functionalities
    runid = bps.runTest(modelname='Victor-ESA-Test-Spam', group=1)
    # showing progress and current statistics
    progress = 0
    try:
        while (progress < 100):
            progress = bps.getRTS(runid)
            time.sleep(1)
    except:
        print("An exception occurred")
    # showing the test result (Pass/Fail)
    # a sleep is put here because we do not immediately get the test results.
    # inserting a sleep to allow for the data to be stored in the database before retrieval
    time.sleep(1)
    bps.getTestResult(runid)
    progress = 100
    print('start')

    print('end')

    # Second test: Steve-WebSec-Test
    runid = bps.runTest(modelname='Steve-WebSec-Test', group=1)
    # showing progress and current statistics
    progress = 0
    try:
        while (progress < 100):
            progress = bps.getRTS(runid)
            time.sleep(1)
    except:
        print("An exception occurred")
    # showing the test result (Pass/Fail)
    # a sleep is put here because we do not immediately get the test results.
    # inserting a sleep to allow for the data to be stored in the database before retrieval
    time.sleep(2)
    bps.getTestResult(runid)

    # Second Test
    runid = bps.runTest(modelname='Victor-Malware-Hash-Test', group=1)
    # showing progress and current statistics
    progress = 0
    try:
        while (progress < 100):
            progress = bps.getRTS(runid)
            time.sleep(1)
    except:
        print("An exception occurred")
    # showing the test result (Pass/Fail)
    # a sleep is put here because we do not immediately get the test results.
    # inserting a sleep to allow for the data to be stored in the database before retrieval
    time.sleep(10)
    bps.getTestResult(runid)
    progress = 100
    print('start')

    print('end')

    # Third Test
    runid = bps.runTest(modelname='Cyber-Landing-Traffic', group=1)
    # showing progress and current statistics
    progress1 = 0
    try:
        while (progress1 < 100):
            progress1 = bps.getRTS(runid)
            time.sleep(1)
    except:
        print("Second exception occurred")

    time.sleep(1)
    bps.getTestResult(runid)

    # logging out
    bps.logout()
    flash('Your attack CL BPS Demo has been launched!', 'success')

    return render_template('about_demo.html', title='test', form=form)


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


@main.route("/about_demo")
def about_demo():
    return render_template('about_demo.html', title='About_demo')


@main.route("/apt")
def apt():
    return render_template('apt.html', title='apt')


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
    bps.reservePorts(slot=1, portList=[0, 1, 2, 3], group=1, force=True)
    # running the canned test 'AppSim' using group 1
    # please note the runid generated. It will be used for many more functionalities
    runid = bps.runTest(modelname='Victor-ESA-Test-Spam', group=1)
    # showing progress and current statistics
    progress = 0
    try:
        while (progress < 100):
            progress = bps.getRTS(runid)
            time.sleep(1)
    except:
        print("An exception occurred")
    # showing the test result (Pass/Fail)
    # a sleep is put here because we do not immediately get the test results.
    # inserting a sleep to allow for the data to be stored in the database before retrieval
    time.sleep(1)
    bps.getTestResult(runid)
    progress = 100
    print('start')

    print('end')

    # Second test: Steve-WebSec-Test
    runid = bps.runTest(modelname='Steve-WebSec-Test', group=1)
    # showing progress and current statistics
    progress = 0
    try:
        while (progress < 100):
            progress = bps.getRTS(runid)
            time.sleep(1)
    except:
        print("An exception occurred")
    # showing the test result (Pass/Fail)
    # a sleep is put here because we do not immediately get the test results.
    # inserting a sleep to allow for the data to be stored in the database before retrieval
    time.sleep(2)
    bps.getTestResult(runid)

    # Second Test
    runid = bps.runTest(modelname='Victor-Malware-Hash-Test', group=1)
    # showing progress and current statistics
    progress = 0
    try:
        while (progress < 100):
            progress = bps.getRTS(runid)
            time.sleep(1)
    except:
        print("An exception occurred")
    # showing the test result (Pass/Fail)
    # a sleep is put here because we do not immediately get the test results.
    # inserting a sleep to allow for the data to be stored in the database before retrieval
    time.sleep(10)
    bps.getTestResult(runid)
    progress = 100
    print('start')

    print('end')

    # Third Test
    runid = bps.runTest(modelname='Cyber-Landing-Traffic', group=1)
    # showing progress and current statistics
    progress1 = 0
    try:
        while (progress1 < 100):
            progress1 = bps.getRTS(runid)
            time.sleep(1)
    except:
        print("Second exception occurred")

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
    username = 'root'
    password = 'C1sc0123@CL'
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=True, allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()
    output = remote_conn.recv(1000)
    print(output)

#    remote_conn.send("/usr/bin/python3 /root/temp/test1.py")
    remote_conn.send("uname -a\r")
    output1 = remote_conn.recv(2000)
    time.sleep(1)
    print(output1)
    flash(output1, 'success')

    return render_template('about.html', title='test', form=form)


@main.route("/attack/3", methods=['GET', 'POST'])
@login_required
def attack3():
    form = PostForm()
    ret = check_output(["python3", "/home/scao/autocli/test2.py"])
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
    bps.reservePorts(slot=1, portList=[0, 1, 2, 3], group=1, force=True)
    # running the canned test 'AppSim' using group 1
    # please note the runid generated. It will be used for many more functionalities
    runid = bps.runTest(modelname='Victor-ESA-Test-Spam', group=1)
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
    ret = check_output(["python3", "/home/scao/autocli/single_bpsProfile.py"])

    flash('Attatck 5 has been launched', 'success')

# Call the brute.bat on the Windows Client


@main.route("/attack/6", methods=['GET', 'POST'])
@login_required
def attack6():
    form = PostForm()
    ip = '172.16.14.37'
    port = 22
    username = 'administrator'
    password = 'C1sc0123'
    cmd = 'brute.bat'

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password)

    stdin, stdout, stderr = ssh.exec_command(cmd)
    outlines = stdout.readlines()
    resp = ''.join(outlines)
    print(resp)
    flash(resp, 'success')

    return render_template('about_demo.html', title='test', form=form)


@main.route("/attack/status", methods=['GET', 'POST'])
@login_required
def attack_status():
    form = PostForm()
    bps = BPS('172.16.14.28', 'admin', bpspassword)
    bps.login()
    ret = bps.runningTestInfo()
    if len(ret) == 2:
        flash('The BPS attack status is not running/starting', 'success')
        # flash(len(ret))

    else:
        progress = re.search('Progress: \[(\d+)\]', ret).groups()[0]

        # print(progress)
        flash('The BPS attack status is: ' + progress + '%', 'success')
        # flash(ret)
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
