# JourneyBot
That Sky [Bot] for thatgamecompany and #thatskygame

## Deployment Checklist
1. Create channels for:
   * Rules
   * Welcome
1. Create member role
1. Create rules message and add **:candle:** reaction
1. Channel permissions:
   * Rules and welcome should be
     * **@everone:** - +read, -send, -add reaction
     * **bot:** +add reaction
   * Any members-only channel should be
     * **@everyone:** -read
     * **members:** +read
1. Config file required. see config.example.json and fill in channel IDs, guild ID, role IDs, SQL creds