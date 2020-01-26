pragma solidity ^0.4.0;

contract poliTricker {
	// A structure to hold the link to an article and its apparent score
	struct Article {
		string link;
		uint score;
	}

	uint public articleCount;
	Article[] articles;

	struct Candidate {
		uint score;
		uint mentions;
	}

	uint candidateCount;
	string[] roster;
	mapping (string => Candidate) public candidates;

	constructor() public {
		articleCount = 0;
	}

	function newCandidate(string _name) public {
		roster[candidateCount] = _name;
		candidates[_name] = Candidate(0, 0);
		candidateCount++;
	}

	function newArticle(string _link, uint _score, string _candidate) public {
		// Adds new Articles along with their scores to the database
		Article memory article = Article(_link, _score);
		articles[articleCount] = article;

		// Calculates the new score of the useers 
		candidates[_candidate].score = candidates[_candidate].score*candidates[_candidate].mentions + _score;
		candidates[_candidate].mentions++;
		candidates[_candidate].score /= candidates[_candidate].mentions;
	}

	function candidateScore(string _name) public returns(uint, uint) {
		return (candidates[_name].score, candidates[_name].mentions);
	}
}
