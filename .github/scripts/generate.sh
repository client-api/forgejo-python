#!/usr/bin/env bash

# Clean up

generated_files_path="./.openapi-generator/FILES"

if [ -f "$generated_files_path" ]; then
    while IFS= read -r generated_file; do

        generated_file="$(echo "$generated_file" | tr -d '\r\n')"

        if [[ "$generated_file" == ".gitignore" || "$generated_file" == ".openapi-generator-ignore" || "$generated_file" == "README.md" || "$generated_file" == ".github" ]]; then
            continue
        fi

        if [ -f "$generated_file" ]; then
            rm -f "$generated_file"
        fi
    done < "$generated_files_path"
fi

# Download generator

if [ ! -f "./.openapi-generator/openapi-generator-cli.jar" ]; then
    xml_string=$(curl -s "https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/maven-metadata.xml")

    if [ -z "$xml_string" ]; then
        echo "Unable to fetch XML metadata."
        exit 1
    fi

    latest_version=$(echo "$xml_string" | grep -oPm1 "(?<=<latest>)[^<]+")
    latest_version_url="https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/${latest_version}/openapi-generator-cli-${latest_version}.jar"

    curl -o "./.openapi-generator/openapi-generator-cli.jar" "$latest_version_url"
fi

# Check Java

output=$(java -version 2>&1)
if [[ "$output" == *"java version"* || "$output" == *"openjdk version"* ]]; then
    echo "Java version: $output"
else
    echo "Java is not found."
    exit 1
fi

# Check Generator Version

output=$(java -jar ./.openapi-generator/openapi-generator-cli.jar version)
if [[ "$output" == "$latest_version" ]]; then
  echo "OpenAPI Generator version: $output"
else
  echo "Unable to verify OpenAPI Generator version"
  exit 1
fi

# Generate

java -jar ./.openapi-generator/openapi-generator-cli.jar generate \
    --input-spec "./.github/specs/openapi.yml" \
    --generator-name "python" \
    --output ./ \
    --enable-post-process-file \
    --git-host "github.com" \
    --git-repo-id "forgejo-python" \
    --git-user-id "client-api" \
    --package-name "clientapi_forgejo" \
    --additional-properties "packageName=clientapi_forgejo,packageUrl=https://github.com/client-api/forgejo-python,packageVersion=1.1.1,projectName=clientapi-forgejo"

# Check if the command was successful
if [ $? -eq 0 ]; then
    echo "Done"
    exit 0
else
    echo "Failed"
    exit 1
fi



