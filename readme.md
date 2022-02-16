2022.02.15
-- -- -- --

:mac: :node: </br>
brew update </br>
brew install node </br>

:truffle: </br>
npm install -g truffle </br>
npm install -g truffle@0.8.11 </br>
set compiler version in truffle-config.js </br>
contract/[contract_name].sol </br>
truffle compile [contract_name] </br>
truffle compile --list          # to see available compiler versions </br>
sudo truffle compile    # download the compiler and then you can continue using non-elevated command truffle compile thereafter </br>
truffle deploy [contract_name] </br>


:Oaclize: </br>
download Oraclize.sol contract #stale versions available from proovable things Ethereum API github @ https://github.com/provable-things/ethereum-api </br>
https://app.provable.xyz/home/test_query # test here


:network config: Ropstein : </br>
npm install --save-dev @truffle/hdwallet-provider </br>
update trufflee-config </br>
npx truffle console --network ropsten </br>
truffle deploy [contract_name] --network ropsten

:eth: test net </br>
use metamask address </br>


:ropsten: project id </br>
https://ethereumico.io/knowledge-base/infura-api-key-guide/ </br>