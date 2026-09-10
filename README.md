# Dynamic Extortion Autopsy

## Forensic Reverse Engineering of Algorithmic Price Discrimination in Bangalore Mobility Platforms

Every commuter in Bangalore has experienced the exact same sinking feeling. You stand under a dripping awning at Silk Board junction or along the outer ring road during a ferocious evening monsoon downpour. Water cascades down the roadway, traffic stalls into an endless sea of red taillights, and your smartphone battery indicator drops below ten percent. You open your preferred ride hailing application to book a cab home. The quote appears on screen, displaying an exorbitant fourfold surge markup. You close the app, wait two minutes, reopen it in desperate hope of a fairer quote, only to watch the fare climb even higher.

For years, technology platforms have insisted that dynamic pricing engines are simple economic balancers reflecting pure supply and demand. They tell the public that prices rise only because many people want rides while few drivers are available on congested roads. Yet everyday observations tell a far more sinister story. If you compare quotes side by side with a colleague standing right next to you heading to the same destination, the prices rarely match. The user holding a flagship phone with single digit battery life routinely receives a significantly higher quote than someone holding an inexpensive device with a full charge. What rideshare platforms describe as efficient market clearing begins to look suspiciously like weaponized desperation.

This project exists to transform an unspoken public suspicion into rigorous mathematical proof. We all intuitively feel exploited when our devices are dying and we have no alternative transit options, but intuition alone cannot hold opaque algorithms accountable. By dissecting the underlying digital mechanics, Dynamic Extortion Autopsy shines a bright light on the covert data points harvested by modern mobile applications. Your battery percentage, the rapid frequency with which you switch between ride apps, and even the retail value of your smartphone hardware are treated not as passive diagnostic metrics, but as high value signals of consumer elasticity and distress.

Commercial ride hailing platforms guard their proprietary pricing dispatch algorithms behind strict corporate secrecy, encrypted application binaries, and private server clusters. Because these production engines remain locked away as corporate trade secrets, direct code inspection is impossible. To overcome this obstacle, this project develops a hybrid synthetic forensic dataset. This architecture fuses authentic physical constraints of Bangalore, including known bottleneck corridors, live traffic congestion multipliers, and torrential monsoon rainfall patterns, with digital user profiling telemetry.

The data generation engine models fifty thousand simulated ride requests across primary tech corridors such as Koramangala, Indiranagar, Whitefield, Bellandur, and Electronic City. Rather than relying on simple linear formulas, the system calculates price surges through multi variable interactions. Physical road delays establish the baseline multiplier, while digital desperation triggers introduce predatory markups. A commuter with a battery level below fifteen percent suffers an immediate pricing penalty. Rapid app reopening events indicate captive demand, compounding the final quote. Hardware profiling further stratifies users, penalizing premium smartphone owners who are algorithmically assumed to possess higher purchasing tolerance.

The repository is structured into modular components designed for reproducible analysis:

* data: Houses the primary forensic dataset detailing ride sessions, physical weather indicators, battery states, device categories, and price markups.
* scripts: Contains the pure vectorized dataset generator script that simulates ride records and prints baseline statistical moments across battery cohorts.
* notebooks: Contains the complete exploratory data analysis notebook executing variance calculations, ride status distributions, hardware tier violin plots, and desperation correlation matrices.

The empirical analysis reveals a stark divergence in financial outcomes. Commuters trapped in critical battery states face a mean algorithmic markup substantially higher than commuters with abundant charge, accompanied by higher variance in quoted fares. The correlation analysis exposes a strong inverse relationship between battery life and price penalties, alongside a strong positive correlation between rapid app reopenings and sudden price escalation. These findings establish that dynamic pricing in modern mobility apps extends far beyond physical road congestion, actively extracting maximum financial surplus from vulnerable commuters when they need transportation the most.

To reproduce the empirical findings locally, execute the following workflow:

1. Clone the repository to your local workstation.
2. Install the necessary data analysis libraries including pandas, numpy, matplotlib, and seaborn.
3. Run the dataset generator script located in the scripts folder to synthesize fresh telemetry data.
4. Launch Jupyter and open the exploratory data analysis notebook located in the notebooks directory to interact with the visualizations and statistical models.

Dynamic Extortion Autopsy operates as an independent open source research initiative dedicated to digital consumer rights and algorithmic transparency. By documenting the exact mathematical pathways through which mobile telemetry can be weaponized against commuters, this project aims to foster public dialogue, encourage regulatory scrutiny over algorithmic pricing practices, and empower consumers with clear empirical awareness.
