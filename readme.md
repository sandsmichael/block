2022.02.15
-- -- -- --

:mac: :node:
brew update
brew install node

:truffle:
npm install -g truffle
npm install -g truffle@0.8.11
set compiler version in truffle-config.js
contract/[contract_name].sol
truffle compile [contract_name]
truffle compile --list          # to see available compiler versions
sudo truffle compile    # download the compiler and then you can continue using non-elevated command truffle compile thereafter
truffle deploy [contract_name]


:Oaclize:
download Oraclize.sol contract #stale versions available from proovable things Ethereum API github @ https://github.com/provable-things/ethereum-api
https://app.provable.xyz/home/test_query # test here


:network config: Ropstein :
npm install --save-dev @truffle/hdwallet-provider
update trufflee-config
npx truffle console --network ropsten

:eth: test net
use metamask address