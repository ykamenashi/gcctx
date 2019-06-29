# gcctx
`gcloud config configurations select` alternative: wanna be an equivalent of `kubectx`

## words dict
* profile
  * equivalent to one of `gcloud config configurations list` entry.
* sub-directory / dir / category
  * virtual(non-gcloud-internal function) separater for a lot of profiles

## To Do
* [ ] duplicate existing profile settings into new profile
* [ ] switch between existing profiles
* [ ] sub-directory style category splitting
* [ ] categoly editing

## command line syntax
### duplicate existing profile to another new (action: COPY)
> gcctx c [profile-origin] [profile-new]

### switch to another profile (action: SELECT)
> gcctx s [profile-name]

### supports sub-directory
> gcctx s [dir-name/profile-name]

#### sub-directory manipuration (action: MOVE)
> gcctx m [profile-name] [dir-name/]

> gcctx m [dir-name/profile-name] [dir-name/profile-name]

## how it works
### `~/.gcloud/active_config` => points name of `configurations` profile
* gcctx manipulates this.

