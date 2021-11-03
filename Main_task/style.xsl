<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform"> 
	<xsl:template match="/">
		<html>
		<table border='1'>
			<tr bgcolor="#CCCCCC">
				<td align="center"><strong><font size="4" color="#0047BA" face="Arial">День</font></strong></td>
				<td align="center"><strong><font size="4" color="#0047BA" face="Arial">Время/неделя</font></strong></td>
				<td align="center"><strong><font size="4" color="#0047BA" face="Arial">Ауд./Корпус	</font></strong></td>
				<td align="center"><strong><font size="4" color="#0047BA" face="Arial">Предмет/Преподаватель</font></strong></td>
				<td align="center"><strong><font size="4" color="#0047BA" face="Arial">Формат занятий</font></strong></td>
			</tr>
			<xsl:for-each select="root/schedule/day/lessons/lesson">
				<tr bgcolor="#F5F5F5">
					<td><xsl:value-of select="short-name-of-day"/></td>
					<td><xsl:value-of select="time-and-weeks"/></td>
					<td><xsl:value-of select="room"/></td>
					<td><xsl:value-of select="name-and-teacher"/></td>
					<td><xsl:value-of select="lesson-format"/></td>
				</tr>
			</xsl:for-each>
		</table>
		</html>
	</xsl:template>
</xsl:stylesheet>