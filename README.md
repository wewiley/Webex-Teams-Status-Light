---


---

<h1 id="webex-teams-status-light">Webex Teams Status Light</h1>
<p>Quarantined at home… working… with kids… you too?  Do your kids seem not to notice whether you are on the phone before barging in with their list of demands, questions, lunch orders, etc?  Yeah mine too.  I was on the phone with my manager the other day and my youngest came straight into my office telling me how his older brother was tormenting him in some way, seemingly unaware that I was actively in a conversation.</p>
<p>Look I get it, in the world of great video devices and collaborating from home, sometimes it’s tough for others to SEE that you are working.  All they see is you sitting at your desk looking at a screen.  There is no visible indicator that you actively on a call, or in a meeting, or just need some time undisturbed.  These indicators are all something we take for granted using Webex Teams.  My colleagues know when I am on the phone, presenting, away, etc.</p>
<p>After the situation with my son and my manager, I started thinking… how can I train them to look at my status before bombarding me with their dialogue, so I started coding.  During the process, I discovered another project on <a href="https://github.com/matthewf01/Webex-Teams-Status-Box">GitHub</a>.  Some of the structure of my code comes from that repository.</p>
<h2 id="getting-started">Getting Started</h2>
<p>These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.</p>
<h3 id="prerequisites">Prerequisites</h3>
<p>Hardware:</p>
<pre><code>- Raspberry Pi  running Raspian
- LED Pixel Ring (https://www.amazon.com/gp/product/B0105VMWRM/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&amp;psc=1)
- Jumper wires
- Soldering equipment 
</code></pre>
<h2 id="raspberry-pi-setup">Raspberry Pi Setup</h2>
<p>This README won’t go into the setup of the Raspberry Pi.  There are way too many tutorials out there for that.  Needless to say, install Raspian with the desktop as all of the programming will happen on the Pi.</p>
<h2 id="wiring-the-project">Wiring the Project</h2>
<p>This may seem daunting to some, but when you break it down, its really not too bad.  In lieu of soldering, you could use alligator clips for prototyping</p>
<h4 id="v-power">5v Power</h4>
<p>There are many ways to power the pixel ring… direct from Pi, using a power supply, etc.  More information on that here <a href="https://learn.adafruit.com/neopixels-on-raspberry-pi">https://learn.adafruit.com/neopixels-on-raspberry-pi</a>.</p>
<p>I chose to wire directly to the Raspberry Pi GPIO header.</p>
<h4 id="pixel-wiring">Pixel Wiring</h4>
<p>This is where the soldering comes in.  You need to solder three wires to the pixel ring.  I used some male to female jumper wires I had laying around, clipped e male end of each and soldered  the following:</p>
<pre><code>- Red wire to Power 5v DC
- Black Wire to Power Signal Ground
- Green Wire to Data Input
</code></pre>
<p><img src="https://github.com/wewiley/WebexTeamsStatusLight/blob/master/photos/IMG_8908.jpg" alt="Image of pixel ring"><br>
Now that the wires are soldered to the pixel ring, we can connect everything together.  For the pixel ring to work correctly, we need to choose a GPIO pin that supports PWM, in my case GPIO 12.<br>
<img src="https://i.stack.imgur.com/yHddo.png" alt="Image of GPIO pins on Pi"></p>
<pre><code>- Red wire (positive) from pixel ring to Raspberry Pi pin 2 or 4.
- Black wire (ground) from pixel ring to Raspberry Pi pin 6.
- Green wire (data) from pixel ring to Raspbery Pi GPIO 12..
</code></pre>
<p><img src="https://github.com/wewiley/WebexTeamsStatusLight/blob/master/photos/zero_wiring.jpg" alt="Image of wiring"></p>
<h2 id="software-requirements">Software Requirements</h2>
<p>This will assume that you have the Raspian OS installed and running on the Raspberry Pi.  The next step will be to install all of the required packages.</p>
<p>Open Terminal and run these commands to install all of the necessary packages:</p>
<pre class=" language-bash"><code class="prism  language-bash"><span class="token function">sudo</span> pip3 <span class="token function">install</span> rpi_ws281x adafruit-circuitpython-neopixel webexteamssdk
<span class="token function">sudo</span> python3 -m pip <span class="token function">install</span> --force-reinstall adafruit-blinka
</code></pre>
<p>All necessary packages should now be installed.</p>
<h2 id="testing-the-pixel-ring">Testing the Pixel Ring</h2>
<p>Included in the repository is test_pixel.py which will aid in verifying your wiring is good.  Open the file in your preferred editor, I use Thonny since its included in the Raspian OS.</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token keyword">import</span> board
<span class="token keyword">import</span> neopixel
pixels <span class="token operator">=</span> neopixel<span class="token punctuation">.</span>NeoPixel<span class="token punctuation">(</span>board<span class="token punctuation">.</span>D12<span class="token punctuation">,</span> <span class="token number">16</span><span class="token punctuation">)</span>

<span class="token keyword">while</span> <span class="token boolean">True</span><span class="token punctuation">:</span>
    pixels<span class="token punctuation">.</span>fill<span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">,</span><span class="token number">200</span><span class="token punctuation">,</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
    pixels<span class="token punctuation">.</span>show<span class="token punctuation">(</span><span class="token punctuation">)</span>
</code></pre>
<p>A few things your need to change/verify:</p>
<pre class=" language-python"><code class="prism  language-python">pixels <span class="token operator">=</span> neopixel<span class="token punctuation">.</span>NeoPixel<span class="token punctuation">(</span>board<span class="token punctuation">.</span>D12<span class="token punctuation">,</span> <span class="token number">16</span><span class="token punctuation">)</span>
</code></pre>
<p>board.D12 refers to the GPIO pin you are using.  If using a different pin, change this number accordingly.  16 refers to the number of pixels on the ring.  If using a different pixel ring, modify this accordingly.</p>
<p>The next thing to point out is the pixels.fill line.  The numbers in () refer to Red, Green, Blue values.  In this example, when the code is executed, the pixel ring should light up all green.  If you want a different color, play with the values 0-255.</p>
<pre class=" language-python"><code class="prism  language-python">pixels<span class="token punctuation">.</span>fill<span class="token punctuation">(</span><span class="token punctuation">(</span><span class="token number">0</span><span class="token punctuation">,</span><span class="token number">200</span><span class="token punctuation">,</span><span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">)</span>
</code></pre>
<h3 id="executing-test_pixel.py">Executing test_pixel.py</h3>
<p>From a terminal session, change directories to where the test_pixel.py resides and execute the following:</p>
<pre class=" language-bash"><code class="prism  language-bash"><span class="token function">sudo</span> python3 test_pixel.py
</code></pre>
<p>In order for the pixels to work, we must execute the code with sudo.  If the pixel lights up, then your wiring is correct.</p>
<h2 id="getting-ready-for-the-big-show">Getting Ready for the Big Show</h2>
<p>Before you can execute the main part of this project and light up the pixels based on your status, you need to do a few things:</p>
<ul>
<li>You need an authorization token to access the Webex Teams API’s.  For testing purposes, you can get a 12hr token, but for production use, I would suggest using a bot access token.  All of this can be found at <a href="https://developer.webex.com/docs/api/getting-started">https://developer.webex.com/docs/api/getting-started</a>.  Copy down your access token:</li>
<li>In order for the API to know which person’s status you want to view, the API needs the PersonID.  You can find your own PersonID by running this GET example: <a href="https://developer.webex.com/docs/api/v1/people/get-my-own-details">https://developer.webex.com/docs/api/v1/people/get-my-own-details</a>.  Copy your id.</li>
</ul>
<p>Using your text editor, open <a href="http://config.py">config.py</a> and enter the information you just retrieved making sure to leave the “” on each and then save the file.</p>
<pre><code>access_token = "your bot access token"
person = "person id"
</code></pre>
<h2 id="edit-teamsstatuslight.py">Edit <a href="http://TeamsStatusLight.py">TeamsStatusLight.py</a></h2>
<p>Just like you did with the pixel test file, open <a href="http://TeamStatusLight.py">TeamStatusLight.py</a> in your preferred editor and make sure the correct GPIO pin and number of pixels are stated:</p>
<pre class=" language-python"><code class="prism  language-python"><span class="token comment">#define the neopixel object by GPIO pin and number of pixels </span>
pixels <span class="token operator">=</span> neopixel<span class="token punctuation">.</span>NeoPixel<span class="token punctuation">(</span>board<span class="token punctuation">.</span>D12<span class="token punctuation">,</span> <span class="token number">16</span><span class="token punctuation">)</span>
</code></pre>
<p>Thats it.  Everything else that is needed is stored in <a href="http://config.py">config.py</a>.  Now you are ready to execute the code.  Make sure <a href="http://TeamsStatusLight.py">TeamsStatusLight.py</a> and <a href="http://config.py">config.py</a> are in the same directory.</p>
<pre class=" language-bash"><code class="prism  language-bash"><span class="token function">sudo</span> python3 TeamsStatusLight.py
</code></pre>
<p>Now you should see feedback in terminal window, and the corresponding light color on the pixel ring.</p>
<pre class=" language-bash"><code class="prism  language-bash">pi@teamsstatus:~/Python/WebexTeamsStatusLight $ <span class="token function">sudo</span> python3 TeamsStatusLight.py 
active
He<span class="token string">'s active! GREEN
Turning green on!
Slept for 5 seconds
active
He'</span>s active<span class="token operator">!</span> GREEN
Turning green on<span class="token operator">!</span>
Slept <span class="token keyword">for</span> 5 seconds
DoNotDisturb
Turning red on<span class="token operator">!</span>
Busy
</code></pre>
<p><img src="https://github.com/wewiley/WebexTeamsStatusLight/blob/master/photos/zero_avail.jpg" alt="Available"><img src="https://github.com/wewiley/WebexTeamsStatusLight/blob/master/photos/zero_busy.jpg" alt="Busy"></p>
<h2 id="coming-soon">Coming Soon</h2>
<p>Next I will be working on an enclosure to mount this outside my door.  Stay tuned.</p>
<h2 id="authors">Authors</h2>
<ul>
<li><strong>Wes Wiley</strong> - <em>Initial work</em> - <a href="https://github.com/wewiley">Wes Wiley</a></li>
</ul>
<h2 id="license">License</h2>
<p>This project is licensed under the MIT License.</p>
<h2 id="acknowledgments">Acknowledgments</h2>
<ul>
<li>Inspiration from <a href="https://github.com/matthewf01">matthewf01</a> <a href="https://github.com/matthewf01/Webex-Teams-Status-Box">Webex-Teams-Status-Box</a></li>
</ul>

