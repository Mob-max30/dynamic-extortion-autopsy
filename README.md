# Dynamic Extortion Autopsy

## Forensic Reverse Engineering of Algorithmic Price Discrimination in Bangalore Mobility Platforms

### The Commuter Nightmare

Every commuter in Bangalore knows this exact situation all too well. 

You stand under a small shop roof at Silk Board junction or along the outer ring road while heavy evening rain pours down. The roads turn into waterlogged rivers, traffic freezes in every direction, and your phone battery suddenly flashes a low power warning below ten percent. 

Here is what happens next:

* You open your ride hailing app to book a cab or auto rickshaw to get home.
* The screen quotes a price that is three or four times the normal rate.
* You close the app and wait a couple of minutes, hoping the price might cool down.
* You reopen the app, only to discover that the price has climbed even higher.

### The Official Story vs The Hidden Reality

Mobility companies have always given the same official explanation to the public:

* They claim that pricing is purely based on supply and demand.
* They say fares go up simply because many riders want cabs and few drivers are on the road.

However, real world observations reveal a much deeper story:

* Two people standing right next to each other requesting the exact same destination often see completely different prices.
* A rider with five percent battery gets quoted a higher price than someone with ninety percent battery.
* A person using a high end flagship phone often sees a higher fare than someone on an inexpensive budget phone.
* What companies call dynamic pricing looks less like fair market balancing and more like weaponized personal urgency.

### Why This Project Matters

This project turns an everyday suspicion into clear mathematical proof.

We all feel frustrated when we sense an app is taking advantage of our low battery or bad weather, but personal feelings alone cannot hold private algorithms accountable. 

Dynamic Extortion Autopsy exposes the hidden digital signals that modern mobility apps can quietly gather:

* Battery Level: Measuring how close your device is to shutting down.
* App Refresh Count: Tracking how many times you open and close the app in panic.
* Device Classification: Checking your phone brand and model to estimate your spending capacity.

These data points are not just innocent device statistics. In an unfair pricing system, they become signals of how desperate you are, allowing an algorithm to charge the absolute maximum price you will tolerate.

### The Challenge and Our Investigation Method

Commercial ride hailing algorithms are closely guarded corporate secrets. Their code is locked inside private company servers, making direct inspection impossible for the public.

To overcome this roadblock, this project builds a realistic hybrid forensic dataset:

* Physical Road Realities: We simulate authentic Bangalore conditions, including major traffic bottlenecks, long travel times, and severe monsoon rain.
* Digital User Profiling: We simulate individual digital behaviors, such as dying batteries, repeated app reopens, and device price tiers.
* Mathematical Verification: By combining road conditions with user telemetry, we can cleanly separate normal traffic surges from unfair predatory markups.

### How The Telemetry and Pricing Model Works

The dataset generator creates fifty thousand simulated ride requests across primary Bangalore tech hubs, including Koramangala, Indiranagar, Whitefield, Bellandur, and Electronic City.

The pricing engine operates through several clear layers:

* Baseline Physical Cost: The regular fare based on total trip distance and travel duration.
* Traffic and Weather Surge: Standard fare increases caused by heavy road congestion and monsoon downpours.
* Battery Level Penalty: An extra price markup triggered when battery drops below fifteen percent, knowing the rider cannot afford to wait.
* Refresh Frequency Penalty: An added price jump when a user repeatedly reopens the app, signaling urgent need.
* Device Hardware Penalty: An additional markup applied to expensive flagship devices based on estimated purchasing power.

### Repository Structure

This repository is organized into clean, dedicated modules:

* data: Stores the primary forensic dataset containing fifty thousand ride records with complete physical and digital attributes.
* scripts: Contains the Python data generator script built using fast vectorized calculations with NumPy and Pandas.
* notebooks: Contains the Jupyter notebook performing full exploratory data analysis, statistical calculations, and visual charts.

### Key Forensic Discoveries

The numbers demonstrate clear patterns of price discrimination:

* Higher Markups for Dying Phones: Commuters with critical battery levels face a much higher average algorithmic markup compared to riders with plenty of battery life.
* Wider Price Variance: Low battery sessions show huge unpredictable price swings, maximizing rider stress.
* Strong Negative Battery Correlation: As battery percentage goes down, the added price markup goes up in a predictable curve.
* Strong Positive Refresh Correlation: The more frequently you open the app to check prices, the steeper the final quote becomes.
* Hardware Tier Discrepancy: Flagship phone users consistently receive higher price distributions compared to budget phone users across identical routes.

### How To Run This Investigation Locally

You can explore the data and run the code on your own machine by following these steps:

1. Clone this repository to your local computer.
2. Install the standard data science libraries including pandas, numpy, matplotlib, and seaborn.
3. Run the dataset generator script in the scripts directory to produce fresh simulation data.
4. Launch Jupyter and open the exploratory notebook in the notebooks directory to interact with the analysis and charts.

### Project Purpose and Community Goal

Dynamic Extortion Autopsy is an independent open source project dedicated to digital consumer rights, fair tech practices, and algorithmic transparency. 

By mapping the exact mathematical ways mobile phone data can be used against everyday riders, this project empowers commuters with clear evidence and encourages open discussion on fair pricing standards.
