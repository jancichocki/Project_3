# Voting Token System

## Authors
- Jan Cichocki
- Betrand Badinga
- Krashawn Ray-el

## Introduction
The Voting Token System is a blockchain-based voting system that leverages the power of Ethereum smart contracts and Python's Streamlit library to create a user-friendly frontend application. This system uses the ERC721 token standard to mint unique voting tokens that represent voting power for stock proxy decisions. Each token is linked to a specific proposal, allowing token holders to cast votes on corporate decisions.

## Features
- **Token Minting**: This feature allows users to mint unique voting tokens associated with specific proposals. Each token represents a vote that can be cast for the proposal it is associated with.
- **Delegation**: Token holders have the ability to delegate their voting rights to another address. This allows for flexibility in decision-making and the potential for proxy voting.
- **Voting**: Token holders or their delegates can cast votes on proposals. This is the core functionality of the system.
- **Real-time Data**: The system integrates real-time stock data fetching to inform users about the current financial status of the company involved in the proposals. This helps users make informed decisions when voting.
- **Transparent Tracking**: All votes and proposals are tracked transparently on the Ethereum blockchain. This ensures the integrity and verifiability of the voting process.

## Technical Stack
- **Solidity**: Used for smart contract development for the ERC721 voting tokens.
- **OpenZeppelin**: A library for secure smart contract development. Utilized for secure contract standards.
- **Ethereum Blockchain**: The platform for deployment of the smart contracts.
- **Python**: Used for backend logic and interaction with the smart contract.
- **Streamlit**: A Python library used for creating the frontend application to interact with the system.
- **Financial Modeling Prep API**: An API service that fetches real-time stock data.

## Installation Guide

### Prerequisites
Before you begin, ensure you have the following installed:
- Node.js and npm
- Python 3.8 or higher
- Streamlit

### Setting Up the Smart Contract
Follow these steps to set up the smart contract:
1. Clone the repository: `git clone <repository_url>`
2. Navigate into the project directory: `cd <project_directory>`
3. Compile the smart contract using Remix IDE.

### Setting Up the Python Environment
Follow these steps to set up the Python environment:
1. Install required Python packages: `pip install -r requirements.txt`
2. Set environment variables in a `.env` file: `cp .env.example .env` and fill in the necessary details.
3. Run the Streamlit application: `streamlit run app.py`

## Usage
Here's how to use the system:
- **Mint Tokens**: Navigate to the Mint section in the Streamlit app, enter the proposal details, and click "Mint".
- **Delegate Votes**: Provide the token ID and the delegate's address to transfer voting rights.
- **Cast Votes**: Select a token ID and vote choice, then submit your vote.
- **View Proposals**: Enter a token ID to retrieve detailed information about the proposal.
