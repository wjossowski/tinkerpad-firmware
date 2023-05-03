dir := $(shell pwd)
src := ${dir}/src
libs := ${dir}/3rdparty
out := /Volumes/CIRCUITPY

init: 
	@cp -r ${libs}/kmk_firmware/kmk ${out}
	@cp -r ${libs}/circuitpython/* ${out}/lib

deinit: clean
	@rm -rf ${out}/kmk
	@rm -rf ${out}/lib/*

flash:
	@mkdir -p ${out}/boards ${out}/layers ${out}/devices
	@cp ${src}/boards/*.py ${out}/boards
	@cp ${src}/layers/*.py ${out}/layers
	@cp ${src}/devices/*.py ${out}/devices
	@cp ${src}/*.py ${out}

clean:
	@rm -rf ${out}/*.py ${out}/layers ${out}/boards
