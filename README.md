# poliTricker - The API to keep politicians off fakenoose

The `poliTricker` database is a contract on the Ethereum network that stores information about a political entity aka the `Candidate`, which contains their name as well as a count of articles that have referred to them. The new articles being added to the database/chain are stored as `Article` type of data. 

The sentiment score of the individual is mapped along with the number of mentions the individual can garner within a struct `Candidate` and the overall sentiment of an article is stored along with it's link in the `Article` struct.

The API provides applications with a simple interface to query data with regards to an individual candidate or entities that are participating in the elections and shows the articles that refer to them.

This interacts with the mobile app and the Zulip bot to provide a good idea about the candidates to a user.