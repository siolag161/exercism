class Bob
  hey: (msg) ->
    m = msg.trim()
    if m == "" then return "Fine. Be that way!"
    else if m.toUpperCase() is m and m.toLowerCase() isnt m then return "Whoa, chill out!"
    else if m.slice(-1) == "?" then return "Sure."
    "Whatever."    
module.exports = Bob
