*** May 25 2022 ------------------------------------------------------------------------------------------------------------------------
 
---  funds ganache wallet for localhost deployments
sudo npm install -g ganache-cli
ganache-cli --defaultBalanceEther 900000000000
ganache-cli --account "0x70f1384b24df3d2cdaca7974552ec28f055812ca5e4da7a0ccd0ac0f8a4a9b00,9000000000000000000000"
--
in truffle-config; use ganache setup with localhost server------>
rpc server-----> HTTP://127.0.0.1:7545
            module.exports = {
            networks: {
                development: {
                host: "127.0.0.1",
                port: 7545,
                network_id: "*",
                }
            }
        }
*network could be 5777 | 7545
https://docs.chain.link/docs/single-word-response/
..................................................
1. create .sol 
cd contracts
<strong> ~~review chainlink oracle and job id in constructor of contract .sol ~~ </strong>
            /**
            * @notice Initialize the link token and target oracle
            *
            * Kovan Testnet details:
            * Link Token: 0xa36085F69e2889c224210F603D836748e7dC0088
            * Oracle: 0x74EcC8Bdeb76F2C6760eD2dc8A46ca5e581fA656 (Chainlink DevRel)
            * jobId: ca98366cc7314957b8c012c72f05aeeb
            *
            */
            constructor() {
                // setPublicChainlinkToken();
                oracle = 0x74EcC8Bdeb76F2C6760eD2dc8A46ca5e581fA656;
                jobId = "ca98366cc7314957b8c012c72f05aeeb";
                fee = 0.1 * 10 ** 18; 
            }
1B. truffle compile
2. create migration .js file
            const RequestPrice = artifacts.require("RequestPrice");

            module.exports = function (deployer) {
            deployer.deploy(RequestPrice);
            };
2B. truffle migrate     (<alternatively> truffle deploy)
    --Migrating is the process of deploying compiled Smart Contracts to the Blockchain.
    -- check ganache after this step to see.

        Deploying 'RequestPrice'
        ------------------------
        ⠋ Blocks: 0            Seconds: 0   > transaction hash:    0xff8b430ec47c1517c1dc5015acda3d2aff71eabf9d72f5d3600cb9b6155c90e6
        > Blocks: 0            Seconds: 0
        > contract address:    0xD0cF0E3DD0F01952D658663f43723a4450A6Bc3B
        > block number:        3
        > block timestamp:     1653456559
        > account:             0x9DfC4E1A1b82D03F44cB664F74E521fd86F89468
        > balance:             99.96913836
        > gas used:            1251727 (0x13198f)
        > gas price:           20 gwei
        > value sent:          0 ETH
        > total cost:          0.02503454 ETH
        > Saving migration to chain.
        > Saving artifacts
        -------------------------------------
        > Total cost:          0.02503454 ETH
        Summary
        =======
        > Total deployments:   2
        > Final cost:          0.03001138 ETH

3A. fund the smart contract by sending link to the contract addy [check balance in truffle stdout / console log]
   > contract address:    0xD0cF0E3DD0F01952D658663f43723a4450A6Bc3B

******
4. interact w contractt using truffle console commands
*******
truffle develop
    -- enter shell (REPL)
let instance = await RequestPrice
    -- view contract details from stdout
    -- attempt to call contract function (i.e. requestPriceData() ... wip ...   )

...LIIIIIIIITTTTTTTTTTTTT...

*** April 2022 ------------------------------------------------------------------------------------------------------------------------

--
truffle unbox smartcontractkit/box
truffle migrate --network kovan --reset
npm install @truffle/hdwallet-provider

---- 

npm i @chainlink/contracts yarn add @chainlink/contracts -- download dependency files localy; set vs code "solidity default workspace compiler" --> local file truffle compile

juanfranblanco/vscode-solidity#178

https://stackoverflow.com/questions/67321111/file-import-callback-not-supported

git clean -df git rm --cached -r . git checkout HEAD

//import "github.com/oraclize/ethereum-api/provableAPI.sol";

https://trufflesuite.com/ganache/

truffle console todolist = await TodoList.deployed() -- use async await for asyncronous interactions todolist todolist.address todolist.tasksCount() tasksCount = await TodoList.tasksCount()

npm install ganache-cli --save-dev node_modules/.bin/ganache-cli | grep Mnemonic npm run ganache curl http://127.0.0.1:8545
-X POST
-H "Content-Type: application/json"
-d '{"jsonrpc": "2.0", "method": "web3_clientVersion"}' npm install concurrently --save-dev npm run start

--

scp: local to ec2 scp -i blah.pem /your/local/file/to/copy user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com:path/to/file

scp: ec2 to local scp -i sandsmichael.pem ubuntu@ec2-54-167-32-57.compute-1.amazonaws.com:/home/ubuntu/xyz.pub /Users/michaelsands/code/block/pyblock/xyz.pub

for aws remember chmod 400 yourPublicKeyFile.pem to make file only readable by root andnot publicly visible

openssl via ubuntu on ec2 sudo apt-get install openssl
generates a private key (.pem): openssl genrsa -out xyz.pem 1024 use the private key to generate a public key (.pub): openssl rsa -in xyz.pem -pubout > xyz.pub

ssh -i "....pem" ubuntu@ec2-54-167-32-57.compute-1.amazonaws.com

mac brew update brew install openssl echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.bash_profile source ~/.bash_profile

2022.02.15

:mac: :node:
brew update
brew install node

:truffle:
npm install -g truffle
npm install -g truffle@0.8.11
set compiler version in truffle-config.js
contract/[contract_name].sol
truffle compile [contract_name]
truffle compile --list # to see available compiler versions
sudo truffle compile # download the compiler and then you can continue using non-elevated command truffle compile thereafter
truffle deploy [contract_name]

:Oaclize:
download Oraclize.sol contract #stale versions available from proovable things Ethereum API github @ https://github.com/provable-things/ethereum-api
https://app.provable.xyz/home/test_query # test here

:network config: Ropstein :
npm install --save-dev @truffle/hdwallet-provider
update trufflee-config
npx truffle console --network ropsten
truffle deploy [contract_name] --network ropsten

:eth: test net
use metamask address

:ropsten: project id
https://ethereumico.io/knowledge-base/infura-api-key-guide/