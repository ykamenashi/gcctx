# gcctx
[`gcloud config configurations activate`](https://cloud.google.com/sdk/gcloud/reference/config/configurations/activate) alternative: Wanna be an equivalent of `kubectx`

## Words dict
* `profile`
  * Equivalent to one of `gcloud config configurations list` entry.
* `sub-directory` / `dir` / `category`
  * Virtual(non-gcloud-internal function) separater for a lot of profiles
* `store`
  * Data-store of gcctx itself.
  * It means `~/.gcctx`

## To Do
* [x] Get selectable profiles
  * [ ] Get selectable profiles (but category filtered)
* [ ] Duplicate existing profile settings into new profile
* [x] Switch between existing profiles
* [ ] Sub-directory style category splitting
* [ ] Category editing

## Command line syntax sample
### Get active config (action: NOW)
> gcctx n

### Get all selectable profiles (action: GET)
> gcctx g

#### Get category-oliented profiles
> gcctx g all
* => show all categories, and selectable profiles
> gcctx g dirs
* => show all dir names
> gcctz g [dir-name]
* => show profiles in dir

### Duplicate existing profile to another new (action: COPY)
> gcctx c [profile-origin] [profile-new]

### Switch to another profile (action: SELECT)
> gcctx s [profile-name]

> gcctx is [profile-name]
* `is` : internal set

#### Switching supports sub-directory
> gcctx s [dir-name/profile-name]

#### Sub-directory manipuration (action: MOVE)
> gcctx m [profile-name] [dir-name/]

> gcctx m [dir-name/profile-name] [dir-name/profile-name]

## How it works
### `~/.gcloud/active_config` => points name of `configurations` profile
* gcctx manipulates this.

### Category definition
* `~/.gcctx`

