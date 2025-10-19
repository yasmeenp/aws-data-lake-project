--Querying data from s3 files in both raw bucket & processed bucket once the data is crawled
SELECT * FROM "youtube_revenue"."tv_channelyasmeen_youtube_raw" limit 10;
SELECT * FROM "youtube_revenue"."modified_tv_channelyasmeen_youtube_processed" limit 10;

