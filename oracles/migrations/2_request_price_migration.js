const RequestPrice = artifacts.require("RequestPrice");

module.exports = function (deployer) {
  deployer.deploy(RequestPrice);
};
