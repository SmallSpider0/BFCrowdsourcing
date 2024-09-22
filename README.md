# BFCrowdsourcing

BFCS is a novel service framework designed to counteract submitter bribery in crowdsourcing. Inspired by receipt-free electronic voting systems, BFCS utilizes a decentralized secure re-encryption protocol to anonymize submissions, thereby eliminating bribery risks by detaching them from submitter identities. 

- **config**
  - bc_keys.json: Blockchain accounts for testing
  - config.yaml: Config file for the project
  - server_list.json: Server list template used during remote testing
- **envs**
  - ipfs: IPFS execution environment
  - mychain: Ethereum private chain environment
  - logs: Logs output by execution environment
- **evaluation**
  - 1_performance_local.py: A sample of Local End-to-end performance evaluation
  - 1_performance_remote.py: A sample of Remote End-to-end performance evaluation
- **prototype**
  - **nodes**
    - base_node.py: Base class for randomizer, requester, and submitter
    - contract_interface.py: Convenient interface for interacting with smart contracts
    - randomizer.py: Implementation of randomizer
    - requester.py: Implementation of requester
    - submitter.py: Implementation of submitter
  - **task**
    - cifar10_tagging.py: Implementation of cifar10_tagging task
    - simple_task.py: A simple task example (array accumulation task)
    - task_interface.py: Abstract class of task, all tasks must implement all methods in this class
  - **thirdparty**
    - **ipfshttpclient**: Utilizing [py-ipfs-http-client](https://github.com/ipfs-shipyard/py-ipfs-http-client) to interact with IPFS
  - **utils**
    - config.py: Used to read configuration files
    - elgamal_encryptor.py: Convenient interface for elgamal encryption related operations (implemented based on elgamal.py)
    - elgamal.py: Elgamal encryption implementation based on PyCrypto
    - log.py: Used for writing logs
    - network.py: Implementation of socket communication between nodes
    - tools.py: Utilities, such as contract deployment, ssh command sending
  - remore_manager.py: Server management program for remote deployment, used to start and stop various nodes as needed
  - system_interface_local.py: Use multi-process to deploy systems locally and provide interactive interfaces
  - system_interface_remote.py: Automatically interact with servers in server_list.json to deploy distributed systems, and provide interactive interfaces
- **solidity**
  - CrowdsourcingContract.sol: Smart contracts used in this system
  - EtherWallet.sol and SimpleContract.sol: Sample contract, used to test the validity of the contract interface


## How to deploy and test BFCrowdsourcing locally

Tested on macOS 14.1.2, to run on other platforms please:

For IPFS, download the binary file from https://github.com/ipfs/kubo and replace the file envs/ipfs/bin/ipfs

For Ethereum, download the binary file from https://geth.ethereum.org/downloads and replace the file envs/mychain/bin/geth


### 1. Clone the souce code

```bash
git clone https://github.com/SmallSpider0/BFCrowdsourcing
cd BFCrowdsourcing
pip install -r requirements.txt
```

### 2. Start the enviroment locally (in terminal 1)

```bash
./start_env.sh init
./start_env.sh up
```

### 3. start and run BFCS locally (in terminal 2)


```bash
cd BFCrowdsourcing
python evaluation/1_performance_local.py
```

Final output
```
2024-01-11 13:59:18,074 INFO: 【Requester】final answer generated 60000 tags 
event/TASK_END
```

### 4. Stop the enviroment (in terminal 1)
```bash
./start_env.sh down
```
