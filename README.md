# SQL-injection CTF
Login using sql injection to acces the website. There you will be able to retrieve the key using your sql querying skills.

To run the ctf you need to follow these steps:

1. clone this git repository. (you can use: VSCODE)
<img width="545" alt="Screenshot 2023-04-24 at 19 27 04" src="https://user-images.githubusercontent.com/104017860/234071833-9a977189-7a73-4cfd-9f5b-221495156f38.png">

click on code then on HTTPS, and copy the address.
<img width="462" alt="Screenshot 2023-04-24 at 19 28 42" src="https://user-images.githubusercontent.com/104017860/234072120-5f28983d-7b6d-4241-9f24-c072fd3137e8.png">

Go to VSCODE paste the address in the bar that appears after you select clone this repository and click enter. 
<img width="740" alt="Screenshot 2023-04-24 at 19 31 15" src="https://user-images.githubusercontent.com/104017860/234072630-d09b690e-071e-41fb-a2f9-9205dcaf68e5.png">

next you need to select a location to clone the repository to, navigate to Desktop.
click new folder, and give the new folder a name.
then click select as repository destination.
<img width="790" alt="Screenshot 2023-04-24 at 19 33 33" src="https://user-images.githubusercontent.com/104017860/234073460-241e1329-deb9-44fe-ab26-84a39d83e871.png">

next you will get a notifaction, click on open.

<img width="397" alt="Screenshot 2023-04-24 at 19 38 51" src="https://user-images.githubusercontent.com/104017860/234074173-96c8ae0c-d42a-4861-9240-0e339508e0f6.png">



2. after you opened the repository you need to open up a terminal (it can take sometime before you can do this).
<img width="834" alt="Screenshot 2023-04-24 at 19 40 30" src="https://user-images.githubusercontent.com/104017860/234074450-be2934b6-090f-47ec-8cc4-8003a48699d9.png">


3. type the following command in the terminal: cd sql

4. start docker up (this can also take sometime, so be patient).
<img width="127" alt="Screenshot 2023-04-24 at 19 42 56" src="https://user-images.githubusercontent.com/104017860/234075096-a26b3b67-ca12-46df-b0fd-581511ba7201.png">

5. type this command in terminal and press enter: docker-compose build

6. next type this command to run the challenge: docker-compose up 

7. Now go to your browser of preference and type the following adress in: http://localhost:8000
(It may take sometime before the website shows up on the adress, try refreshing a few times if it doesn't show up)

Good Luck with the Challenge!
