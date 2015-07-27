## Deployment

deploy each module seperately as one would do normally

```
appcfg.py --oauth2 -A topsidelacrosseapp update {module_directory}
```

then update the dispatch file like so

```
appcfg.py update_dispatch {dispatch_directory}
```