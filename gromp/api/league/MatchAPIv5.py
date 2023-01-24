#
# MIT License
#
# Copyright (c) 2023 Wilhelm Ågren
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# File created: 2023-01-23
# Last updated: 2023-01-23
#

from gromp.api import BaseLeagueAPI

__all__ = (
    'MatchAPIv5',
)

URL = {
    'puuid': '{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids',
    'matchId': '{region}.api.riotgames.com/lol/match/v5/matches/{matchId}',
}

class MatchAPIv5(BaseLeagueAPI):
    def __init__(self, platform='euw1', region='europe'):
        super().__init__(platform=platform, region=region)
    
    def puuid(self, token, puuid):
        http_response = self.get(
            token,
            URL['puuid'],
            params={
                '{puuid}': puuid,
                '{region}': self._region,
            }
        )
        return http_response

    def matchId(self, token, matchId):
        http_response = self.get(
            token,
            URL['matchId'],
            params={
                '{matchId}': matchId,
                '{region}': self._region,
            }
        )
        return http_response