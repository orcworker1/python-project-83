CREATE TABLE urls (
    id  SERIAL PRIMARY KEY,
    name varchar(255),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE url_checks (
    id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    url_id INTEGER REFERENCES urls(id) ,
    status_code integer,
    h1 TEXT,
    title TEXT ,
    description TEXT ,
    created_at TIMESTAMP DEFAULT NOW()
);



