Postmortem: August 15, 2024 Outage: The Tale of the Overworked Server

Duration of the Outage:
 🕒 Time Flies, Especially When You are Down!
 From 3:00 PM to 4:30 PM UTC on August 15, 2024, we experienced a rollercoaster ride. Unfortunately, it was not fun. This ride lasted 1 hour and 30 minutes, during which 60% of our users were stuck in a virtual traffic jam, with pages not loading and transactions stuck in a never-ending loop.
Impact:
 🚧 When a Server Says “Nope!”
 Imagine being in a car on a highway and suddenly hitting a traffic jam caused by a single stubborn car. That is precisely what happened, but digitally. Our web application slowed to a crawl, leaving users frustrated and stranded on blank screens or error pages. It was like trying to order pizza during the Super Bowl — lots of hunger, no delivery.
Root Cause: The Tale of a Rogue Load Balancer
🔄 When the Load Balancer Plays Favorites
 Picture this: Our load balancer, supposed to distribute traffic evenly across all servers, decided to play favorites. Instead of sharing the load, it directed most of the traffic to one poor server, causing it to wave a little white flag and crash. The result? It is a digital meltdown of epic proportions.
Timeline of Events: A Comedy of Errors
•	3:00 PM: Monitoring System Shouts “Mayday!”
 Our automated monitoring system started waving red flags with high latency alerts. Think of it as the digital equivalent of your mom texting you 17 times because you have not called her back.
•	3:05 PM: Engineer on Duty: “I Got This!”
 Heroically sipping their third cup of coffee, an engineer was paged and jumped into action. The initial guess? “It is just a traffic spike, no biggie. Let us throw more servers at it.”
•	3:10 PM: More Servers? More Problems!
 The servers were scaled, but the situation did not improve. It was like adding more lanes to a highway but keeping the same bottleneck.
•	3:20 PM: The Logs Never Lie
 Our engineer turned detective, digging into server logs and noticing something fishy — traffic was unevenly distributed. Aha! The load balancer was the culprit.
•	3:35 PM: Enter the DevOps Squad
 The issue was handed over to our DevOps team, the tech world’s SWAT team. They confirmed the misconfiguration and began correcting it.
•	4:00 PM: Balance Restored
 The load balancer was reconfigured, spreading the traffic love across all servers. Things began to return to normal, like the calm after a storm.
•	4:30 PM: All Systems Go
 Monitoring confirmed that everything was back to normal. Crisis averted, but not forgotten.
Root Cause and Resolution: A Happy Ending (With a Lesson)
Root Cause:
 A tiny, sneaky misconfiguration in the load balancer’s settings caused this mess. Directing traffic to a single server created an overload our system could not handle.
Resolution:
 We updated the configuration file, ran some tests, and confirmed that the load balancer was once again a team player, distributing traffic evenly across all servers. Peace was restored in the digital world.
Corrective and Preventative Measures: How We Will Avoid Another Digital Disaster
Improvements:
•	Pre-Deployment Configuration Checks:
 Before we make any changes, we’ll double-check configurations to prevent rogue settings from slipping through.
•	Enhanced Monitoring:
 We will set up detailed monitoring to catch imbalances before they become problematic.
•	Training:
 Engineers will receive extra training on load balancer configurations to avoid future mishaps.
Tasks:
•	Patch the Configuration File:
 We will ensure that the configuration file is patched and locked down.
•	Automated Tests:
 We will develop tests to verify load balancer settings automatically.
•	Secondary Alerts:
 An additional alert system will help detect uneven traffic distribution in real time.
•	Configuration Reviews:
 Regular reviews of load balancer settings across all environments will keep us on track.
 



