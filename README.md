# PatronPal
Project submission for Hack the 6ix hackathon at Toronto Metropolitan University.


Inspiration:
Creators are now more than ever asking for Patreons, donations, and support. But the vast majority of consumers don’t partake in this. 
This isn’t because consumers don’t want to support their favourite creators - it’s just that the cost of doing so would be astronomically high. 
$10 for 15 creators per month leads to $150 a month - no one wants to pay THAT much… especially now with inflation and the job market. 
At the same time, Youtube and other platforms do not pay enough to support smaller creators. 
This led to us coming up with an idea for consumers to set aside a certain amount of money they would like to be allocated to their favourite creators. 
This could be something as low as $5 - $10. The application would then automatically allocate the money. 
The user, of course, will be able to customize everything and have the final say in where their money goes. 
This lets consumers feel good about themselves for supporting their favourite creators while not breaking the bank.


What it does:
Our project aims to help consumers support their favourite creators affordably. 
The browser extension pulls data from supported platforms (such as, but not limited to Youtube, Medium, and Substack) and calculates analytics. 
To combat certain creators uploading/posting much more frequently than others, the application checks how frequently the creator uploads and weighs that against how much you watch that creator. 
A minute watch time of a creator who uploads 30-minute videos daily is worth much less than a minute of a creator who uploads a 20-minute video every month. 
Thus, a slice of the $10 pie or so would be allocated accordingly.

In addition, the consumer can allocate a set amount of their “pie” to certain creators. 
For example, a consumer paying $15 a month can choose a number of channels (let’s say two, and they decide they want to pay $1.50 each). 
This amount is not adjusted by our metrics, and our application works with the remaining $12 and allocates it accordingly.

However, with it being almost fully customizable, the user has the final say in where their money goes.


How we built it:
We built it using a front-end built with HTML, CSS, with tailwind framework. The back-end was built through Flask and Python. 


Challenges we ran into


Accomplishments that we're proud of


What we learned
We dived deeper into how to use tailwind and integrate Flask and other products together. 


What’s next for PatronPal
Calculating how to split up the “pie” using more metrics so that it could be better reflective of what the user would want to pay each creator if they had the time to allocate their dollars. 
