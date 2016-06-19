var browserify = require('gulp-browserify');
var gulp = require('gulp');
var gutil = require('gulp-util');
var nib = require('nib');
var rename = require('gulp-rename');
var sourcemaps = require('gulp-sourcemaps');
var stylus = require('gulp-stylus');


var paths = {
    styl: ['kegbot/media/styles/**/*.styl'],
    coffee: ['kegbot/media/scripts/**/*.coffee', 'kegbot/media/scripts/**/*.cjsx'],
    app_styl: ['kegbot/media/styles/app.styl'],
    app_coffee: ['kegbot/media/scripts/app.cjsx'],
    output: './kegbot/static/'
};

gulp.task('styles', function(){
    return gulp.src(paths.app_styl)
        .pipe(sourcemaps.init())
            .pipe(stylus({
                'use': [nib()],
                'import': ['nib']
            }))
        .pipe(sourcemaps.write('./maps', {sourceRoot: null}))
        .pipe(gulp.dest(paths.output));
});

gulp.task('scripts', function(){
    return gulp.src(paths.app_coffee, {read: false})
        .pipe(sourcemaps.init())
            .pipe(browserify({
                'transform': ['coffee-reactify'],
                'extensions': ['.coffee', '.cjsx']
            }))
        .pipe(sourcemaps.write(paths.output))
        .pipe(rename('app.js'))
        .pipe(gulp.dest(paths.output));
});

gulp.task('build', ['scripts', 'styles']);

gulp.task('watch', ['build'], function(cb){
    gulp.watch(paths.styl, ['styles']);
    gulp.watch(paths.coffee, ['scripts']);
});
