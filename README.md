### Test and Lint

```
# Same goes for test
./pants lint :: # Runs linter on the entire codebase
./pants lint ./app_layer/: # Runs linter on the app_layer project
./pants --changed-since=HEAD lint # Runs linter on files changed since last commit
```

### Run

```
./pants run ./app_layer/: # Run the application layer
```

### Packaging

```
./pants package ./app_layer/: # Package the application layer to a PEX file in the dist dir
./pants --changes-since=origin/main package # Package all apps with changes to dist
```

### How would I do CI

Directly run in a workflow
```
./pants --changed-since=origin/main lint
./pants --changed-since=origin/main test
```


### CD????