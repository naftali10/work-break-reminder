# Work Break Reminder

I'm striving to motivate myself to incorporate work breaks
into my routine. These breaks hold significant value
as they enhance both my productivity and overall well-being.
Unlike other applications that often proved overly intrusive
or bothersome, I've meticulously crafted a solution that
strikes the ideal balance between gentle encouragement
and motivation. This solution involves a subtle pop-up reminder
that reappears every minute, displaying carefully phrased sentences
that deeply resonate with me, serving as a continuous source
of inspiration.  

![Pre-Break Popup1.png](docs%2FPre-Break%20Popup1.png)
## Features
- Infinite 1-hour timer
- Timer reset with Alt+F12
- Beeps and popup upon timer finish
- Reminder popup window:
  - Is on top
  - Can be minimized
  - Re-pops once a minute
- No quick dismiss - at leased 2 user interactions, 3 minutes apart, are needed to dismiss a reminder

# Code
## Flow
![Program Flow.png](docs%2FProgram%20Flow.png)

1. Upon program initiation, it initiates a 1-hour timer (referred to as the "major wait") that can be reset by pressing Alt + F12 on the keyboard.
2. After the 1-hour timer elapses, two beeps will emanate from the speakers, followed by an unavoidable popup appearing 20 seconds later.
3. The initial pre-break popup presents the user with three choices:
   1. Ignore: The popup will reappear a minute later in a recurring fashion.
   2. Postpone: It will reappear after a 3-minute wait (referred to as the "minor wait").
   3. Start break: After a 3-minute wait (known as the "break wait"), a post-break popup will appear.  
4. The subsequent post-break popup offers the following options:
   1. Confirm break: Initiates the 1-hour ("major wait") timer to start the break.
   2. Deny break: Returns to the pre-break popup.
   3. Confirm unintentional break: Equivalent to option 1, starting the 1-hour timer.

![Pre-Break Popup2.png](docs%2FPre-Break%20Popup2.png)

![Post-Break Popup.png](docs%2FPost-Break%20Popup.png)
## Clean Code and TDD
I found developing this app as an opportunity to cultivate best coding practices:  
- Test Driven Design - each class has its own unit test
- Clean Code - small functions, and classes that obey Single Responsibility Principal 