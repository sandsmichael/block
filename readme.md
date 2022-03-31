
scp: local to ec2
scp -i blah.pem /your/local/file/to/copy user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com:path/to/file

scp: ec2 to local
scp -i sandsmichael.pem ubuntu@ec2-54-167-32-57.compute-1.amazonaws.com:/home/ubuntu/xyz.pub /Users/michaelsands/code/block/pyblock/xyz.pub

for aws remember chmod 400 yourPublicKeyFile.pem to make file  only readable by root andnot publicly visible

openssl via ubuntu on ec2
sudo apt-get install openssl        
generates a private key (.pem):         openssl genrsa -out xyz.pem 1024
use the private key to generate a public key (.pub):    openssl rsa -in xyz.pem -pubout > xyz.pub


ssh -i "....pem" ubuntu@ec2-54-167-32-57.compute-1.amazonaws.com









mac
brew update
brew install openssl
echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile





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