const ProvableRequest = artifacts.require("ProvableRequest");

module.exports = function (deployer) {
  deployer.deploy(ProvableRequest);
};
