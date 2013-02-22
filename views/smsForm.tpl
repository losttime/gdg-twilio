<!DOCTYPE html>
<html>
	<head>
	</head>
	<body>
		<form action="/smsSend" method="POST">
			<input type="text" name="toNum" value="" placeholder="to" />
			%for record in froms:
				<input type="text" name="fromNum" value="{{record['number']}}" placeholder="from" />
			%end
			<textarea name="body" placeholder="Whatcha wanna say?"></textarea>
			<button type="submit">Submit</button>
		</form>
		%if message:
			<p>{{message}}</p>
		%end
	</body>
</html>