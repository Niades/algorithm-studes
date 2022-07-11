cd:
	cd src/$(p)

prepare:
	cp .git-hooks/* .git/hooks/
run-bs:
	python3 ./src/binary-search/binary-search-1.py
run-dfs:
	python3 ./src/dfs/dfs-1.py
run-bfs:
	python3 ./src/bfs/bfs-1.py
test-bfs:
	cd ./src/bfs && python3 -m unittest test
test-all:
	for PROJECT in *;    												  \
	do                    												  \
		for ALGO in *;   												  \
		do			     												  \
			cd ./src/$($$PROJECT)/$($$ALGO);						  \
			pwd;									   					  \
		done;		     												  \
	done;			     												  \