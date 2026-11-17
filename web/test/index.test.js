const test = require("node:test");
const assert = require("node:assert");
const { pickName } = require("../index");

test("pickName reads nested name", () => {
  assert.strictEqual(pickName({ profile: { name: "Ada" } }), "Ada");
  assert.strictEqual(pickName({}), "anonymous");
});
