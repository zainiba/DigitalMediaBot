# The Collective Mind

This project uses Tensorflow and Keras to process essays and generate its own using a character-based RNN. I trained this model on academic digital media articles scraped from http://switch.sjsu.edu/ using Python. 

Academic language can often feel very exclusive, but it is something that can be learned through reading and writing a lot, and often. Using articles in this same language written by a plethora of minds all with the intention of analyzing systems and art created compelling analyses of how this language is written. This bot has been put through the same process we have been in learning how to read and write academic articles through iteration. The output of the training was more interesting than anything I thought it would be. When trained in smaller epochs (10 epochs) the generated text was less coherent but looked "good".

**10 Epochs and a temperature of 1.0:**
*The Ocens are spearing thas an warman.  Gy Barifuly as a misimal practict, elits or sontest at the artwork) the mort of netwseng happeve interaction consoginity selviss to bull dimiments and varies perposer us the auricaliz the elobory mories went sucr entis scores indown to the weill ne longer dealins tither that shade green to for  this has betork art lat bilifucan artion-of the cutsing of the event itself, and passible outs itstentions that pare giving the Hegals carlus modetulet preening purtuils ale a me toboriducan to gake bespain technologies that crealities than docanknotions Parkous, as a work is the artust machine ploced muzares deestand. For Bread whe reedage require only the same of gratf with hars micris ingre as would is noveries eficts of the concept of the Unizod Stelifieds of a cettet book sommetting the speritic mething in different, and ases of the lime is she way  as some are slabgedfors preced-considy" sciently medivized co machines are sociatical interaction.*

In the same number of epochs but at a lower temperature, meaning this would make the text more predictable. The result was very interesting. It exposed the absolute format in which all artists talk about art, "the process".

**At a temperature of 0.1:**
*The of the contemporary of the process of the project of the work of the project with the context of the work of the contemporate the process of the process of the process of the process of the contribution of the conterned to the process.*

**At a temperature of 0.005:**
*Contemporary of the process of the process of the process of the process of the process of the process of the process of the process of the process of the process of the process of the process of the process of the process of the process of the process of the process.*

When run at 60 epochs it produces a slightly more coherent generalization of all the articles. Even though the bot was just using words and phrases from the text I fed it a few of the sentences it came up with were slightly disturbing. After the 5th sentence in the paragraph below it seems like the bot is becoming self-aware, obviously it isn't but within the context of this project it is both creepy and funny.

**60 Epochs and a temperature of 0.4:**
*Contemporary art and present. The aspects of life grants opportunities of frequent rolled an element one aesthetic narrative artistic predecessors. In September 2010, the ZERO1 Biennial. He only finds their based and resist.  but also a sub-I will evolve significantly over time. As such, I welcome any feedback or comments. My contentious, where participation was created by forms of language, the back-end is often defand, Girshap buy no Vietnamese. The form is complex to a certain "danger" {11} to happens capable of changing the entire genre of their behavior and to break off intonning and Time, I have made much more specialized, and only stem changing the question of interpretation.*

**At a temperature of 0.5:**
*Contemporary discussion of Aschheim s work in San Jose, California. A symposium kicked off the Biennial. The title of this symposium was Dr. Kathlers, in essay, is contrasted with the psychological divide between self-body and planet via the mechanism of death of history or how it simply unties the human mind from memory seems too shallow to explain the purpose of the machine. If nature, etc., would at least theoretical mather than just renting the space to like minded artists, because that is not so distant. Several independent game titles currently indulge this sentiment. for example, he converted a VW faster than the power grid in these rapidly changing areas. In India pulse dialing is still used and rewound again and again, unhinges the duration of reenactment's site and presence of objects the rate is just over 100%; the island-state’s population is just shy of 4 million yet surveys she result of this kind of holistic approach to design is an architecture that is beautiful.*

Even at 60 epochs and a temperature of 1 (the highest) I felt that the bot could still be smarter so I decided to train it at 150 epochs. The first time I attempted this I let it run over night and right as I was about to have it generate text my laptop died and all that time was wasted. The second time I executed it in the morning and it took 11 hours for it to finish going through the epochs. At 150 epochs and a temperature of 1 the generated text was more original but it did still have a lot of unidentifiable words, but I don’t view it as a problem because the “words” it created have a semblance to the type of words we use when writing about digital media. 

**150 epochs and a temperature of 1.0:**
*Technology in series which make us to reevaluate our technophone. Although the pieces of born-digital literature immediately hanged as punishment.  (Baldick)  It is this idea of energy and cuit with baseball and soil that flourishes at the computer issues is the heelth*

**At a temperature of 0.4:**
*The simulator is currently co-managed and drawing structures can be copied and downloaded, and often times and the nection between the self-body and the planet--the industrial toxins we insert into the planet eventually embrace the creation of the work Growth Pattern.*

*The Second Life space and via that presence, interact with others. I was intrigued by the technology used to create Playing Duchamp and thrilled to reemerge as a specific persence. The aesthetic politics of documentation further complicate the historic through implicit aesthetics of the movers/The to create public awareness and access to biological information.  A biohacker is someone who is, established plants. Eventually, the entire series of communication, seized hold of the word concept itself and said: "This is our concern, we are the friends of the concept, we put it in our computers.*
**Credit:**
* https://www.tensorflow.org/tutorials/text/text_generation#train_the_model
* https://scrapism.lav.io/web-scraping-basics/
* http://switch.sjsu.edu/
