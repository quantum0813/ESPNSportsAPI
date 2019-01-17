import datetime
import json
import requests


class EventsDate:
    def __init__(self, date, season_type):
        self.date = date
        self.season_type = season_type


class Weather:
    def __init__(self, display_value, temperature, condition_id):
        self.display_value = display_value
        self.temperature = temperature
        self.condition_id = condition_id


class Link:
    def __init__(self, language, rel, href, text, short_text, is_external, is_premium):
        self.language = language
        self.rel = rel
        self.href = href
        self.text = text
        self.short_text = short_text
        self.is_external = is_external
        self.is_premium = is_premium


class VideoDeviceRestrictions:
    def __init__(self, type, devices):
        self.type = type
        self.devices = devices


class VideoTracking:
    def __init__(self, sport_name, league_name, coverage_type, tracking_name, tracking_id):
        self.sport_name = sport_name
        self.league_name = league_name
        self.coverage_type = coverage_type
        self.tracking_name = tracking_name
        self.tracking_id = tracking_id


class Video:
    def __init__(self, id, source, headline, thumbnail, duration, tracking, device_restrictions, links):
        self.id = id
        self.source = source
        self.headline = headline
        self.thumbnail = thumbnail
        self.duration = duration
        self.tracking = tracking
        self.device_restrictions = device_restrictions
        self.links = links


class Headline:
    def __init__(self, description, type, short_link_text, video):
        self.description = description
        self.type = type
        self.short_link_text = short_link_text
        self.video = video


class GeoBroadcast:
    def __init__(self, type_id, type_short_name, market_id, market_type, media_short_name, lang, region):
        self.type_id = type_id
        self.type_short_name = type_short_name
        self.market_id = market_id
        self.market_type = market_type
        self.media_short_name = media_short_name
        self.lang = lang
        self.region = region


class Group:
    def __init__(self, id, name, short_name, is_conference):
        self.id = id
        self.name = name
        self.short_name = short_name
        self.is_conference = is_conference


class Broadcast:
    def __init__(self, market, names):
        self.market = market
        self.names = names


class StatusType:
    def __init__(self, id, name, state, completed, description, detail, short_detail):
        self.id = id
        self.name = name
        self.state = state
        self.completed = completed
        self.description = description
        self.detail = detail
        self.short_detail = short_detail


class Status:
    def __init__(self, clock, display_clock, period, type):
        self.clock = clock
        self.display_clock = display_clock
        self.period = period
        self.type = type


class Record:
    def __init__(self, name, abbreviation, type, summary):
        self.name = name
        self.abbreviation = abbreviation
        self.type = type
        self.summary = summary


class Athlete:
    def __init__(self, id, full_name, display_name, short_name, links, jersey, headshot, position_abbreviation, team_id, active):
        self.id = id
        self.full_name = full_name
        self.display_name = display_name
        self.short_name = short_name
        self.links = links
        self.jersey = jersey
        self.headshot = headshot
        self.position_abbreviation = position_abbreviation
        self.team_id = team_id
        self.active = active


class Leader:
    def __init__(self, display_value, athlete, team_id):
        self.display_value = display_value
        self.athlete = athlete
        self.team_id = team_id


class LeaderType:
    def __init__(self, name, display_name, short_display_name, abbreviation, leaders):
        self.name = name
        self.display_name = display_name
        self.short_display_name = short_display_name
        self.abbreviation = abbreviation
        self.leaders = leaders


class Statistic:
    def __init__(self, name, abbreviation, display_value):
        self.name = name
        self.abbreviation = abbreviation
        self.display_value = display_value


class Team:
    def __init__(self, id, uid, location, name, abbreviation, display_name, short_display_name, color, alternate_color, is_active, venue_id, links, logo, conference_id):
        self.id = id
        self.uid = uid
        self.location = location
        self.name = name
        self.abbreviation = abbreviation
        self.display_name = display_name
        self.short_display_name = short_display_name
        self.color = color
        self.alternate_color = alternate_color
        self.is_active = is_active
        self.venue_id = venue_id
        self.links = links
        self.logo = logo
        self.conference_id = conference_id


class Competitor:
    def __init__(self, id, uid, type, order, home_away, winner, team, score, line_scores, statistics, leaders, current_curated_rank, records):
        self.id = id
        self.uid = uid
        self.type = type
        self.order = order
        self.home_away = home_away
        self.winner = winner
        self.team = team
        self.score = score
        self.line_scores = line_scores
        self.statistics = statistics
        self.leaders = leaders
        self.current_curated_rank = current_curated_rank
        self.records = records


class Venue:
    def __init__(self, id, full_name, address_city, address_state, capacity, indoor):
        self.id = id
        self.full_name = full_name
        self.address_city = address_city
        self.address_state = address_state
        self.capacity = capacity
        self.indoor = indoor


class Competition:
    def __init__(self, id, uid, date, attendance, time_valid, neutral_site, conference_competition, recent, venue, competitors, notes, status, broadcasts, groups, start_date, geo_broadcasts, headlines):
        self.id = id
        self.uid = uid
        self.date = date
        self.attendance = attendance
        self.time_valid = time_valid
        self.neutral_site = neutral_site
        self.conference_competition = conference_competition
        self.recent = recent
        self.venue = venue
        self.competitors = competitors
        self.notes = notes
        self.status = status
        self.broadcasts = broadcasts
        self.groups = groups
        self.start_date = start_date
        self.geo_broadcasts = geo_broadcasts
        self.headlines = headlines


class Event:
    def __init__(self, id, uid, date, name, short_name, season_year, season_type, competitions, links, weather, status):
        self.id = id
        self.uid = uid
        self.date = date
        self.name = name
        self.short_name = short_name
        self.season_year = season_year
        self.season_type = season_type
        self.competitions = competitions
        self.links = links
        self.weather = weather
        self.status = status


class SeasonType:
    def __init__(self, id, type, name, abbreviation):
        self.id = id
        self.type = type
        self.name = name
        self.abbreviation = abbreviation


class Season:
    def __init__(self, year, start_date, end_date, type):
        self.year = year
        self.start_date = start_date
        self.end_date = end_date
        self.type = type


class League:
    def __init__(self, id, uid, name, abbreviation, midsize_name, slug, season, calendar_type, calendar_is_whitelist, calendar_start_date, calendar_end_date, calendar):
        self.id = id
        self.uid = uid
        self.name = name
        self.abbreviation = abbreviation
        self.midsize_name = midsize_name
        self.slug = slug
        self.season = season
        self.calendar_type = calendar_type
        self.calendar_is_whitelist = calendar_is_whitelist
        self.calendar_start_date = calendar_start_date
        self.calendar_end_date = calendar_end_date
        self.calendar = calendar


class ESPNScoreboard:
    def __init__(self, sport_name, league_name):
        """
        Constructs a new instance of the scoreboard with provided sport and league name.

        The following is a list of sports and corresponding leagues:

        Sport           Leagues
        -----           -------
        football        college-football, nfl
        basketball      nba, wnba, womens-college-basketball, mens-college-basketball
        baseball        mlb
        hockey          nhl
        soccer          eng.1, usa.1

        For soccer, 'eng.1' is EPL and 'usa.1' is MLS

        :param sport_name: The type of sport for which you want to construct the scoreboard.
        :param league_name: The name of the league for the specified sport.
        """
        if sport_name == "football":
            if league_name not in ["college-football", "nfl"]:
                raise ValueError("League name should be one of the following: [college-football, nfl]")
        elif sport_name == "basketball":
            if league_name not in ["nba", "wnba", "womens-college-basketball", "mens-college-basketball"]:
                raise ValueError("League name should be one of the following: [nba, wnba, womens-college-basketball, mens-college-basketball]")
        elif sport_name == "baseball":
            if league_name != "mlb":
                raise ValueError("League name must be mlb")
        elif sport_name == "hockey":
            if league_name != "nhl":
                raise ValueError("League name must be nhl")
        elif sport_name == "soccer":
            if league_name not in ["eng.1", "usa.1"]:
                raise ValueError("League name should be one of the following: [eng.1, usa.1]")
        else:
            raise ValueError("Unsupported sport type")

        self.sport_name = sport_name
        self.league_name = league_name
        self.SCOREBOARD_ENDPOINT = f"http://site.api.espn.com/apis/site/v2/sports/{self.sport_name}/{self.league_name}/scoreboard"

    def _parse_video_links(self, video_links):
        return video_links

    def _parse_video_device_restrictions(self, device_restrictions_obj):
        type = None
        devices = None

        if "type" in device_restrictions_obj:
            type = device_restrictions_obj["type"]
        if "devices" in device_restrictions_obj:
            devices = device_restrictions_obj["devices"]

        return VideoDeviceRestrictions(type, devices)

    def _parse_video_tracking(self, video_tracking_obj):
        sport_name = None
        league_name = None
        coverage_type = None
        tracking_name = None
        tracking_id = None

        if "sportName" in video_tracking_obj:
            sport_name = video_tracking_obj["sportName"]
        if "leagueName" in video_tracking_obj:
            league_name = video_tracking_obj["leagueName"]
        if "coverageType" in video_tracking_obj:
            coverage_type = video_tracking_obj["coverageType"]
        if "trackingName" in video_tracking_obj:
            tracking_name = video_tracking_obj["trackingName"]
        if "trackingId" in video_tracking_obj:
            tracking_id = video_tracking_obj["trackingId"]

        return VideoTracking(sport_name, league_name, coverage_type, tracking_name, tracking_id)

    def _parse_competition_headline_video(self, video_arr):
        videos = []

        id = None
        source = None
        headline = None
        thumbnail = None
        duration = None
        tracking = None
        device_restrictions = None
        links = None

        for video in video_arr:
            if "id" in video:
                id = video["id"]
            if "source" in video:
                source = video["source"]
            if "headline" in video:
                headline = video["headline"]
            if "thumbnail" in video:
                thumbnail = video["thumbnail"]
            if "duration" in video:
                duration = video["duration"]
            if "tracking" in video:
                tracking = self._parse_video_tracking(video["tracking"])
            if "deviceRestrictions" in video:
                device_restrictions = self._parse_video_device_restrictions(video["deviceRestrictions"])
            if "links" in video:
                links = self._parse_video_links(video["links"])

            videos.append(Video(id, source, headline, thumbnail, duration, tracking, device_restrictions, links))

        return videos


    def _parse_competition_headlines(self, competition_headlines_arr):
        headlines = []

        description = None
        type = None
        short_link_text = None
        video = None

        for headline in competition_headlines_arr:
            if "description" in headline:
                description = headline["description"]
            if "type" in headline:
                type = headline["type"]
            if "shortLinkText" in headline:
                short_link_text = headline["shortLinkText"]
            if "video" in headline:
                video = self._parse_competition_headline_video(headline["video"])

            headlines.append(Headline(description, type, short_link_text, video))

        return headlines

    def _parse_competition_geo_broadcasts(self, competition_geo_broadcasts_arr):
        geo_broadcasts = []

        type_id = None
        type_short_name = None
        market_id = None
        market_type = None
        media_short_name = None
        lang = None
        region = None

        for geo_broadcast in competition_geo_broadcasts_arr:
            if "type" in geo_broadcast:
                if "id" in geo_broadcast["type"]:
                    type_id = geo_broadcast["type"]["id"]
                if "shortName" in geo_broadcast["type"]:
                    type_short_name = geo_broadcast["type"]["shortName"]
            if "market" in geo_broadcast:
                if "id" in geo_broadcast["market"]:
                    market_id = geo_broadcast["market"]["id"]
                if "type" in geo_broadcast["market"]:
                    market_type = geo_broadcast["market"]["type"]
            if "media" in geo_broadcast:
                if "shortName" in geo_broadcast["media"]:
                    media_short_name = geo_broadcast["media"]["shortName"]
            if "lang" in geo_broadcast:
                lang = geo_broadcast["lang"]
            if "region" in geo_broadcast:
                region = geo_broadcast["region"]

            geo_broadcasts.append(GeoBroadcast(type_id, type_short_name, market_id, market_type, media_short_name, lang, region))

        return geo_broadcasts

    def _parse_groups(self, groups_obj):
        id = None
        name = None
        short_name = None
        is_conference = None

        if "id" in groups_obj:
            id = groups_obj["id"]
        if "name" in groups_obj:
            name = groups_obj["name"]
        if "shortName" in groups_obj:
            short_name = groups_obj["shortName"]
        if "isConference" in groups_obj:
            is_conference = groups_obj["isConference"]

        return Group(id, name, short_name, is_conference)

    def _parse_competition_broadcasts(self, competition_broadcasts_arr):
        broadcasts = []

        market = None
        names = None

        for broadcast in competition_broadcasts_arr:
            if "market" in broadcast:
                market = broadcast["market"]
            if "names" in broadcast:
                names = broadcast["names"]

            broadcasts.append(Broadcast(market, names))

        return broadcasts

    def _parse_competition_notes(self, competition_notes_arr):
        return competition_notes_arr

    def _parse_links(self, links_arr):
        links = []

        language = None
        rel = None
        href = None
        text = None
        short_text = None
        is_external = None
        is_premium = None

        for link in links_arr:
            if "language" in link:
                language = link["language"]
            if "rel" in link:
                rel = link["rel"]
            if "href" in link:
                href = link["href"]
            if "text" in link:
                text = link["text"]
            if "shortText" in link:
                short_text = link["shortText"]
            if "isExternal" in link:
                is_external = link["isExternal"]
            if "isPremium" in link:
                is_premium = link["isPremium"]

            links.append(Link(language, rel, href, text, short_text, is_external, is_premium))

        return links

    def _parse_team(self, team_obj):
        id = None
        uid = None
        location = None
        name = None
        abbreviation = None
        display_name = None
        short_display_name = None
        color = None
        alternate_color = None
        is_active = None
        venue_id = None
        links = None
        logo = None
        conference_id = None

        if "id" in team_obj:
            id = team_obj["id"]
        if "uid" in team_obj:
            uid = team_obj["uid"]
        if "location" in team_obj:
            location = team_obj["location"]
        if "name" in team_obj:
            name = team_obj["name"]
        if "abbreviation" in team_obj:
            abbreviation = team_obj["abbreviation"]
        if "displayName" in team_obj:
            display_name = team_obj["displayName"]
        if "shortDisplayName" in team_obj:
            short_display_name = team_obj["shortDisplayName"]
        if "color" in team_obj:
            color = team_obj["color"]
        if "alternateColor" in team_obj:
            alternate_color = team_obj["alternateColor"]
        if "isActive" in team_obj:
            is_active = team_obj["isActive"]
        if "venue" in team_obj:
            if "id" in team_obj["venue"]:
                venue_id = team_obj["venue"]["id"]
        if "links" in team_obj:
            self._parse_links(team_obj["links"])
        if "logo" in team_obj:
            logo = team_obj["logo"]
        if "conferenceId" in team_obj:
            conference_id = team_obj["conferenceId"]

        return Team(id, uid, location, name, abbreviation, display_name, short_display_name, color, alternate_color, is_active, venue_id, links, logo, conference_id)

    def _parse_line_scores(self, line_scores_arr):
        line_scores = []

        for line_score in line_scores_arr:
            line_scores.append(line_score["value"])

        return line_scores

    def _parse_statistics(self, statistics_arr):
        statistics = []

        name = None
        abbreviation = None
        display_value = None

        for statistic in statistics_arr:
            if "name" in statistic:
                name = statistic["name"]
            if "abbreviation" in statistic:
                abbreviation = statistic["abbreviation"]
            if "displayValue" in statistic:
                display_value = statistic["displayValue"]

            statistics.append(Statistic(name, abbreviation, display_value))

        return statistics

    def _parse_athlete_links(self, athlete_links_arr):
        links = []

        for link in athlete_links_arr:
            if "href" in link:
                links.append(link["href"])

        return links

    def _parse_athlete(self, athlete_obj):
        id = None
        full_name = None
        display_name = None
        short_name = None
        links = None
        jersey = None
        headshot = None
        position_abbreviation = None
        team_id = None
        active = None

        if "id" in athlete_obj:
            id = athlete_obj["id"]
        if "fullName" in athlete_obj:
            full_name = athlete_obj["fullName"]
        if "displayName" in athlete_obj:
            display_name = athlete_obj["displayName"]
        if "shortName" in athlete_obj:
            short_name = athlete_obj["shortName"]
        if "links" in athlete_obj:
            links = self._parse_athlete_links(athlete_obj["links"])
        if "jersey" in athlete_obj:
            jersey = athlete_obj["jersey"]
        if "headshot" in athlete_obj:
            headshot = athlete_obj["headshot"]
        if "position" in athlete_obj:
            if "abbreviation" in athlete_obj["position"]:
                position_abbreviation = athlete_obj["position"]["abbreviation"]
        if "team" in athlete_obj:
            if "id" in athlete_obj["team"]["id"]:
                team_id = athlete_obj["team"]["id"]
        if "active" in athlete_obj:
            active = athlete_obj["active"]

        return Athlete(id, full_name, display_name, short_name, links, jersey, headshot, position_abbreviation, team_id, active)

    def _parse_leaders(self, leaders_arr):
        leaders = []

        display_value = None
        athlete = None
        team_id = None

        for leader in leaders_arr:
            if "displayValue" in leader:
                display_value = leader["displayValue"]
            if "athlete" in leader:
                athlete = self._parse_athlete(leader["athlete"])
            if "team" in leader:
                if "id" in leader["team"]:
                    team_id = leader["team"]["id"]

            leaders.append(Leader(display_value, athlete, team_id))

        return leaders

    def _parse_leader_types(self, leader_types_arr):
        leader_types = []

        name = None
        display_name = None
        short_display_name = None
        abbreviation = None
        leaders = None

        for leader_type in leader_types_arr:
            if "name" in leader_type:
                name = leader_type["name"]
            if "displayName" in leader_type:
                display_name = leader_type["displayName"]
            if "shortDisplayName" in leader_type:
                short_display_name = leader_type["shortDisplayName"]
            if "abbreviation" in leader_type:
                abbreviation = leader_type["abbreviation"]
            if "leaders" in leader_type:
                leaders = self._parse_leaders(leader_type["leaders"])

            leader_types.append(LeaderType(name, display_name, short_display_name, abbreviation, leaders))

        return leader_types

    def _parse_records(self, records_arr):
        records = []

        name = None
        abbreviation = None
        type = None
        summary = None

        for record in records_arr:
            if "name" in record:
                name = record["name"]
            if "abbreviation" in record:
                abbreviation = record["abbreviation"]
            if "type" in record:
                type = record["type"]
            if "summary" in record:
                summary = record["summary"]

            records.append(Record(name, abbreviation, type, summary))

        return records

    def _parse_competitors(self, competitors_arr):
        competitors = []

        id = None
        uid = None
        type = None
        order = None
        home_away = None
        winner = None
        team = None
        score = None
        line_scores = None
        statistics = None
        leaders = None
        current_curated_rank = None
        records = None

        for competitor in competitors_arr:
            if "id" in competitor:
                id = competitor["id"]
            if "uid" in competitor:
                uid = competitor["uid"]
            if "type" in competitor:
                type = competitor["type"]
            if "order" in competitor:
                order = competitor["order"]
            if "homeAway" in competitor:
                home_away = competitor["homeAway"]
            if "winner" in competitor:
                winner = competitor["winner"]
            if "team" in competitor:
                team = self._parse_team(competitor["team"])
            if "score" in competitor:
                score = competitor["score"]
            if "linescores" in competitor:
                line_scores = self._parse_line_scores(competitor["linescores"])
            if "statistics" in competitor:
                statistics = self._parse_statistics(competitor["statistics"])
            if "leaders" in competitor:
                leaders = self._parse_leader_types(competitor["leaders"])
            if "curatedRank" in competitor:
                if "current" in competitor["curatedRank"]:
                    current_curated_rank = competitor["curatedRank"]["current"]
            if "records" in competitor:
                records = self._parse_records(competitor["records"])

            competitors.append(Competitor(id, uid, type, order, home_away, winner, team, score, line_scores, statistics, leaders, current_curated_rank, records))

        return competitors

    def _parse_venue(self, venue_obj):
        id = None
        full_name = None
        address_city = None
        address_state = None
        capacity = None
        indoor = None

        if "id" in venue_obj:
            id = venue_obj["id"]
        if "fullName" in venue_obj:
            full_name = venue_obj["fullName"]
        if "address" in venue_obj:
            if "city" in venue_obj["address"]:
                address_city = venue_obj["address"]["city"]
            if "state" in venue_obj["address"]:
                address_state = venue_obj["address"]["state"]
        if "capacity" in venue_obj:
            capacity = venue_obj["capacity"]
        if "indoor" in venue_obj:
            indoor = venue_obj["indoor"]

        return Venue(id, full_name, address_city, address_state, capacity, indoor)

    def _parse_status_type(self, status_type_obj):
        id = None
        name = None
        state = None
        completed = None
        description = None
        detail = None
        short_detail = None

        if "id" in status_type_obj:
            id = status_type_obj["id"]
        if "name" in status_type_obj:
            name = status_type_obj["name"]
        if "state" in status_type_obj:
            state = status_type_obj["state"]
        if "completed" in status_type_obj:
            completed = status_type_obj["completed"]
        if "description" in status_type_obj:
            description = status_type_obj["description"]
        if "detail" in status_type_obj:
            detail = status_type_obj["detail"]
        if "shortDetail" in status_type_obj:
            short_detail = status_type_obj["shortDetail"]

        return StatusType(id, name, state, completed, description, detail, short_detail)

    def _parse_status(self, status_obj):
        clock = None
        display_clock = None
        period = None
        type = None

        if "clock" in status_obj:
            clock = status_obj["clock"]
        if "displayClock" in status_obj:
            display_clock = status_obj["displayClock"]
        if "period" in status_obj:
            period = status_obj["period"]
        if "type" in status_obj:
            type = self._parse_status_type(status_obj["type"])

        return Status(clock, display_clock, period, type)

    def _parse_weather(self, event_weather_obj):
        display_value = None
        temperature = None
        condition_id = None

        if "displayValue" in event_weather_obj:
            display_value = event_weather_obj["displayValue"]
        if "temperature" in event_weather_obj:
            temperature = event_weather_obj["temperature"]
        if "conditionId" in event_weather_obj:
            condition_id = event_weather_obj["conditionId"]

        return Weather(display_value, temperature, condition_id)

    def _parse_event_competitions(self, event_competitions_arr):
        competitions = []

        id = None
        uid = None
        date = None
        attendance = None
        time_valid = None
        neutral_site = None
        conference_competition = None
        recent = None
        venue = None
        competitors = None
        notes = None
        status = None
        broadcasts = None
        groups = None
        start_date = None
        geo_broadcasts = None
        headlines = None

        for competition in event_competitions_arr:
            if "id" in competition:
                id = competition["id"]
            if "uid" in competition:
                uid = competition["uid"]
            if "date" in competition:
                date = competition["date"]
            if "attendance" in competition:
                attendance = competition["attendance"]
            if "timeValid" in competition:
                time_valid = competition["timeValid"]
            if "neutralSite" in competition:
                neutral_site = competition["neutralSite"]
            if "conferenceCompetition" in competition:
                conference_competition = competition["conferenceCompetition"]
            if "recent" in competition:
                recent = competition["recent"]
            if "venue" in competition:
                venue = self._parse_venue(competition["venue"])
            if "competitors" in competition:
                competitors = self._parse_competitors(competition["competitors"])
            if "notes" in competition:
                notes = self._parse_competition_notes(competition["notes"])
            if "status" in competition:
                status = self._parse_status(competition["status"])
            if "broadcasts" in competition:
                broadcasts = self._parse_competition_broadcasts(competition["broadcasts"])
            if "groups" in competition:
                groups = self._parse_groups(competition["groups"])
            if "startDate" in competition:
                start_date = competition["startDate"]
            if "geoBroadcasts" in competition:
                geo_broadcasts = self._parse_competition_geo_broadcasts(competition["geoBroadcasts"])
            if "headlines" in competition:
                headlines = self._parse_competition_headlines(competition["headlines"])

            competitions.append(Competition(id, uid, date, attendance, time_valid, neutral_site, conference_competition, recent, venue, competitors, notes, status, broadcasts, groups, start_date, geo_broadcasts, headlines))

        return competitions

    def _parse_season_type(self, season_type_obj):
        id = None
        type = None
        name = None
        abbreviation = None

        if "id" in season_type_obj:
            id = season_type_obj["id"]
        if "type" in season_type_obj:
            type = season_type_obj["type"]
        if "name" in season_type_obj:
            name = season_type_obj["name"]
        if "abbreviation" in season_type_obj:
            abbreviation = season_type_obj["abbreviation"]

        return SeasonType(id, type, name, abbreviation)

    def _parse_season(self, season_obj):
        year = None
        start_date = None
        end_date = None
        type = None

        if "year" in season_obj:
            year = season_obj["year"]
        if "startDate" in season_obj:
            start_date = season_obj["startDate"]
        if "endDate" in season_obj:
            end_date = season_obj["endDate"]
        if "type" in season_obj:
            type = self._parse_season_type(season_obj["type"])

        return Season(year, start_date, end_date, type)

    """
    This function gets a scoreboard for the date specified and returns the resulting objects.
    
    :param date: A string in the format "YYYYMMDD" or a Python datetime object
    """
    def get_scoreboard(self, date):
        date_str = ""
        if type(date) is datetime.datetime:
            date_str = date.strftime("%Y%m%d")
        elif type(date) is str:
            date_str = date
        payload = {'dates': date_str}

        req = requests.get(self.SCOREBOARD_ENDPOINT, params=payload)
        parsed_json = json.loads(req.text)

        leagues = []
        if "leagues" in parsed_json and isinstance(parsed_json["leagues"], list):
            for league in parsed_json["leagues"]:
                id = None
                uid = None
                name = None
                abbreviation = None
                midsize_name = None
                slug = None
                season = None
                calendar_type = None
                calendar_is_whitelist = None
                calendar_start_date = None
                calendar_end_date = None
                calendar = None

                if "id" in league:
                    id = league["id"]
                if "uid" in league:
                    uid = league["uid"]
                if "name" in league:
                    name = league["name"]
                if "abbreviation" in league:
                    abbreviation = league["abbreviation"]
                if "midsizeName" in league:
                    midsize_name = league["midsizeName"]
                if "slug" in league:
                    slug = league["slug"]
                if "season" in league:
                    season = self._parse_season(league["season"])
                if "calendarType" in league:
                    calendar_type = league["calendarType"]
                if "calendarIsWhitelist" in league:
                    calendar_is_whitelist = league["calendarIsWhitelist"]
                if "calendarStartDate" in league:
                    calendar_start_date = league["calendarStartDate"]
                if "calendarEndDate" in league:
                    calendar_end_date = league["calendarEndDate"]
                if "calendar" in league:
                    calendar = league["calendar"]

                leagues.append(League(id, uid, name, abbreviation, midsize_name, slug, season, calendar_type, calendar_is_whitelist, calendar_start_date, calendar_end_date, calendar))

        events = []
        if "events" in parsed_json and isinstance(parsed_json["events"], list):
            for event in parsed_json["events"]:
                id = None
                uid = None
                date = None
                name = None
                short_name = None
                season_year = None
                season_type = None
                competitions = None
                links = None
                weather = None
                status = None

                if "id" in event:
                    id = event["id"]
                if "uid" in event:
                    uid = event["uid"]
                if "date" in event:
                    date = event["date"]
                if "name" in event:
                    name = event["name"]
                if "shortName" in event:
                    short_name = event["shortName"]
                if "season" in event:
                    if "year" in event["season"]:
                        season_year = event["season"]["year"]
                    if "type" in event["season"]:
                        season_type = event["season"]["type"]
                if "competitions" in event:
                    competitions = self._parse_event_competitions(event["competitions"])
                if "links" in event:
                    links = self._parse_links(event["links"])
                if "weather" in event:
                    weather = self._parse_weather(event["weather"])
                if "status" in event:
                    status = self._parse_status(event["status"])

                events.append(Event(id, uid, date, name, short_name, season_year, season_type, competitions, links, weather, status))

        return { 'leagues': leagues, 'events': events }
