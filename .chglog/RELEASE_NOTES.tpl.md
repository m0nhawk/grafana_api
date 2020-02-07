{{range .Versions}}
{{range .CommitGroups}}
### {{.Title}}
{{range .Commits}}
* {{if ne .Scope ""}}**{{.Scope}}:** {{end}}{{.Subject}} ({{ .Hash.Short }}){{end}}
{{end}}{{if .RevertCommits}}
### Reverts
{{range .RevertCommits}}
* {{.Revert.Header}}{{end}}
{{end}}{{if .MergeCommits}}
### Pull Requests
{{range .MergeCommits}}
* {{.Header}}{{end}}
{{end}}{{range .NoteGroups}}
### {{.Title}}
{{range .Notes}}
{{.Body}}
{{end}}
{{end}}
{{end}}