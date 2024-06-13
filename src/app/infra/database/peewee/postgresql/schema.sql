-- Active: 1718281456553@@localhost@5432@dev_media
CREATE TABLE developers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    github_username VARCHAR(255),
    twitter_username VARCHAR(255),
    instagram_username VARCHAR(255),
    youtube_channel VARCHAR(255),
    avatar_url VARCHAR(255)
);

CREATE TABLE social_media_records (
    id SERIAL PRIMARY KEY,
    developer_id INTEGER REFERENCES developers(id),
    github_followers_count INTEGER DEFAULT "Indisponível",
    twitter_followers_count INTEGER DEFAULT "Indisponível",
    instagram_followers_count INTEGER DEFAULT "Indisponível",
    youtube_subscribers_count INTEGER DEFAULT "Indisponível",
    github_repos_count INTEGER DEFAULT "Indisponível",
    github_stars_count INTEGER DEFAULT "Indisponível",
    instagram_posts_count INTEGER DEFAULT "Indisponível",
    instagram_likes_count INTEGER DEFAULT "Indisponível",
    twitter_retweets_count INTEGER DEFAULT "Indisponível",
    twitter_likes_count INTEGER DEFAULT "Indisponível",
    youtube_views_count INTEGER DEFAULT "Indisponível",
    youtube_videos_count INTEGER DEFAULT "Indisponível",
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);


SELECT * FROM developers;

SELECT * FROM social_media_records;