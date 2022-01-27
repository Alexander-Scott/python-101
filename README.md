# Running the unit tests

```bash
python3 -m unittest discover is_week_day
```

# Running python coverage

```bash
coverage run --source yaml_loader_module/ -m unittest discover yaml_loader_module
coverage report -m
```

# Goals for 25/01/2022

- [x] Get 100% test coverage for the new `yaml_loader` module.
- [ ] Extend our CI to also run on the `yaml_loader` module.
- [ ] Split up our current CI job into two jobs: one for pycoverage and one for pylint. 
- [ ] The branch protection rules for the Github repo should be updated to reflect the new job names.

# just for a new pr
