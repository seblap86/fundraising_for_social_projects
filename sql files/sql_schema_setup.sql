USE fundraise_social;

# Setting constraints
ALTER TABLE projects
ADD PRIMARY KEY (project_id);

ALTER TABLE topics
ADD PRIMARY KEY (topic_id);

ALTER TABLE topic_relationships
ADD FOREIGN KEY (project_id) REFERENCES projects(project_id);

ALTER TABLE topic_relationships
ADD FOREIGN KEY (topic_id) REFERENCES topics(topic_id);