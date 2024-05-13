# Voting Token System

## Authors
- Jan Cichocki
- Betrand Badinga
- Krashawn Rey-el

## Project Overview
This project implements a blockchain-based voting system using Ethereum smart contracts and a Python Streamlit frontend application. It leverages the ERC721 token standard to create unique voting tokens that represent voting power for stock proxy decisions. Each token is linked to a specific proposal, allowing token holders to cast votes on corporate decisions.

## Features
- **Token Minting**: Users can mint unique voting tokens associated with specific proposals.
- **Delegation**: Token holders can delegate their voting rights to another address.
- **Voting**: Token holders or their delegates can cast votes on proposals.
- **Real-time Data**: Integrates real-time stock data fetching to inform users about the current financial status of the company involved in the proposals.
- **Transparent Tracking**: All votes and proposals are tracked transparently on the Ethereum blockchain.

## Technical Stack
- **Solidity**: Smart contract development for the ERC721 voting tokens.
- **OpenZeppelin**: Utilized for secure contract standards.
- **Ethereum Blockchain**: Deployment of smart contracts.
- **Python**: Backend logic and interaction with the smart contract.
- **Streamlit**: Frontend application to interact with the system.
- **Financial Modeling Prep API**: Fetches real-time stock data.

## Installation Guide

### Prerequisites
- Node.js and npm
- Truffle Suite
- Ganache (for a personal blockchain)
- Python 3.8 or higher
- Streamlit

### Setting Up the Smart Contract
1. Clone the repository:
2. Navigate into the project directory:
3. Install Truffle:
4. Compile the smart contract:
5. Start Ganache and migrate the contract:

### Setting Up the Python Environment
1. Install required Python packages:
2. Set environment variables in a `.env` file:
3. Run the Streamlit application:

## Usage
- **Mint Tokens**: Navigate to the Mint section in the Streamlit app, enter the proposal details, and click "Mint".
- **Delegate Votes**: Provide the token ID and the delegate's address to transfer voting rights.
- **Cast Votes**: Select a token ID and vote choice, then submit your vote.
- **View Proposals**: Enter a token ID to retrieve detailed information about the proposal.

## Project Structure
- `contracts/`: Contains the Solidity smart contracts.
- `migrations/`: Truffle migration scripts for deploying contracts.
- `app.py`: Streamlit frontend application.
- `utils/`: Helper scripts and utility functions.
