#!/usr/bin/node
exports.callMeMoby = function (q, theFunction) {
  for (let a = 0; a < q; a++) theFunction();
};
