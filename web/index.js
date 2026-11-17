const _ = require("lodash");

function pickName(user) {
  return _.get(user, "profile.name", "anonymous");
}

module.exports = { pickName };
