pragma solidity ^0.5.17;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract VotingToken is ERC721Full {
    struct Proposal {
        uint256 proposalId;
        string proposalTitle;
        string proposalDescription;
        address proposalAuthor;
        uint256 proposalTimestamp;
        string proposalStatus;
    }

    struct Vote {
        uint256 voteId;
        address voterAddress;
        uint256 voteTimestamp;
        string voteChoice;
    }

    struct Delegate {
        address delegateAddress;
        uint256 delegatedTokens;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => Vote) public votes;
    mapping(address => Delegate) public delegates;
    mapping(uint256 => address) public tokenDelegates;

    constructor() public ERC721Full("VotingToken", "VOTE") {}

    // Mint a new voting token (proposal)
    function mintVotingToken(address voter, string memory proposalTitle, string memory proposalDescription) public returns (uint256) {
        uint256 newTokenId = totalSupply();
        _mint(voter, newTokenId);
        _setTokenURI(newTokenId, proposalTitle);

        // Create a new proposal and store it in the proposals mapping
        proposals[newTokenId] = Proposal({
            proposalId: newTokenId,
            proposalTitle: proposalTitle,
            proposalDescription: proposalDescription,
            proposalAuthor: voter,
            proposalTimestamp: now,
            proposalStatus: "Open"
        });

        return newTokenId;
    }

    // Delegate voting power to another address
    function delegateVote(uint256 tokenId, address delegate) public {
        require(ownerOf(tokenId) == msg.sender, "Only the owner can delegate this token");
        tokenDelegates[tokenId] = delegate;
        delegates[delegate].delegateAddress = delegate;
        delegates[delegate].delegatedTokens++;
    }

    // Get proposal details
    function getProposalDetails(uint256 tokenId) public view returns (uint256, string memory, string memory, address, uint256, string memory) {
        Proposal memory proposal = proposals[tokenId];
        return (proposal.proposalId, proposal.proposalTitle, proposal.proposalDescription, proposal.proposalAuthor, proposal.proposalTimestamp, proposal.proposalStatus);
    }

    // Cast a vote
    function castVote(uint256 tokenId, string memory voteChoice) public {
        require(ownerOf(tokenId) == msg.sender || tokenDelegates[tokenId] == msg.sender, "You do not have voting rights for this token");
        votes[tokenId] = Vote({
            voteId: tokenId,
            voterAddress: msg.sender,
            voteTimestamp: now,
            voteChoice: voteChoice
        });
    }

    // Get vote details
    function getVoteDetails(uint256 tokenId) public view returns (uint256, address, uint256, string memory) {
        Vote memory vote = votes[tokenId];
        return (vote.voteId, vote.voterAddress, vote.voteTimestamp, vote.voteChoice);
    }
}