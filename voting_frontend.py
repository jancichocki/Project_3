import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import requests

# Load environment variables
load_dotenv()

# Connect to the Ethereum blockchain network using Web3
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Connect to the Financial Modeling Prep API for stock data
API_KEY = "paHmylabXhtMMqNv2fW9FXZhHpgEToy5"

def fetch_stock_data(symbol):
    """Fetch stock data from Financial Modeling Prep API."""
    url = f"https://financialmodelingprep.com/api/v3/profile/{symbol}?apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Load the smart contract ABI and address
@st.cache(allow_output_mutation=True)
def load_contract():
    abi_path = Path('contracts/compiled/voting_abi.json')  # Adjust the ABI path if needed
    with abi_path.open() as f:
        voting_abi = json.load(f)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")
    return w3.eth.contract(address=contract_address, abi=voting_abi)

# Load the VotingToken contract
contract = load_contract()

# Streamlit Interface
st.title("Stock Voting Token Management System")

# Section for Stock Data
symbol = st.text_input("Enter the stock symbol (e.g., AAPL, GOOGL):", value="AAPL")
if st.button("Retrieve Stock Data"):
    data = fetch_stock_data(symbol.upper())
    if data and len(data) > 0:
        data = data[0]
        st.write(f"**Company Name:** {data.get('companyName')}")
        st.write(f"**Exchange:** {data.get('exchangeShortName')}")
        st.write(f"**Stock Price:** ${data.get('price')}")
        st.write(f"**Market Cap:** {data.get('mktCap')}")
        st.write(f"**Description:** {data.get('description')[:300]}...")  # show first 300 characters
    else:
        st.error("Could not retrieve data. Check the stock symbol and try again.")

# Section for Voting on Stock Proposals
voter_accounts = w3.eth.accounts
voter = st.selectbox("Select Voter Account", voter_accounts)

proposal_title = st.text_input("Proposal Title", value="Enter Proposal Title")
proposal_description = st.text_area("Proposal Description", value="Enter Description of the Proposal.")

if st.button("Mint Voting Token"):
    try:
        new_token_id = contract.functions.totalSupply().call()
        tx_receipt = contract.functions.mintVotingToken(voter, proposal_title, proposal_description).transact({'from': voter, 'gas': 1000000})
        st.write(f"Minted Voting Token with Transaction Hash: {tx_receipt.hex()}")
        st.write(f"New Token ID: {new_token_id}")
    except Exception as e:
        st.error(f"Error minting voting token: {str(e)}")

token_id = st.number_input("Token ID for Voting Operations", value=0, step=1)

if st.button("Delegate Vote"):
    delegate_address = st.text_input("Delegate Address")
    try:
        contract.functions.delegateVote(token_id, delegate_address).transact({'from': voter, 'gas': 1000000})
        st.write(f"Delegated Token ID {token_id} to {delegate_address}")
    except Exception as e:
        st.error(f"Error delegating vote: {str(e)}")

if st.button("Cast Vote"):
    vote_choice = st.selectbox("Vote Choice", ["Yes", "No", "Abstain"])
    try:
        contract.functions.castVote(token_id, vote_choice).transact({'from': voter, 'gas': 1000000})
        st.write(f"Voted '{vote_choice}' for Token ID {token_id}")
    except Exception as e:
        st.error(f"Error casting vote: {str(e)}")

if st.button("Get Proposal Details"):
    try:
        proposal_data = contract.functions.getProposalDetails(token_id).call()
        st.write(f"Proposal ID: {proposal_data[0]}")
        st.write(f"Title: {proposal_data[1]}")
        st.write(f"Description: {proposal_data[2]}")
        st.write(f"Author: {proposal_data[3]}")
        st.write(f"Timestamp: {proposal_data[4]}")
        st.write(f"Status: {proposal_data[5]}")
    except Exception as e:
        st.error(f"Error retrieving proposal details: {str(e)}")

